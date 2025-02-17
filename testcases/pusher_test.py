# PyAlgoTrade
#
# Copyright 2011-2018 Gabriel Martin Becedillas Ruiz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. moduleauthor:: Gabriel Martin Becedillas Ruiz <gabriel.becedillas@gmail.com>
"""

import unittest
import threading
import datetime

from jgtpyalgotrade.websocket import pusher
from jgtpyalgotrade.websocket import client


class WebSocketClient(pusher.WebSocketClient):
    def __init__(self):
        pusher.WebSocketClient .__init__(self, "de504dc5763aeef9ff52", maxInactivity=1)
        self.__errors = 0
        self.__unknown_events = 0
        self.__connected = None

    def __checkStop(self):
        if self.__errors == 0:
            return
        if self.__unknown_events == 0:
            return
        # Give it some time to send ping messages.
        if self.__connected is None or (datetime.datetime.now() - self.__connected).total_seconds() < 3:
            return

        self.close()

    def onConnectionEstablished(self, event):
        pusher.WebSocketClient.onConnectionEstablished(self, event)
        self.__connected = datetime.datetime.now()
        self.sendPong()
        self.subscribeChannel("invalid channel")
        self.subscribeChannel("order_book")
        self.subscribeChannel("live_trades")

    def onError(self, event):
        self.__errors += 1
        self.__checkStop()

    def onUnknownEvent(self, event):
        self.__unknown_events += 1
        self.__checkStop()

    def stop(self):
        self.close()


class WebSocketClientThread(client.WebSocketClientThreadBase):
    def __init__(self):
        threading.Thread.__init__(self)
        self.__wsclient = None

    def run(self):
        super(WebSocketClientThread, self).run()

        # We need to build the WebSocketClient right in the thread since it has thread affinity.
        self.__wsclient = WebSocketClient()
        self.__wsclient.connect()
        self.__wsclient.startClient()

    def stop(self):
        self.__wsclient.stop()


class TestCase(unittest.TestCase):
    def test_pusher(self):
        thread = WebSocketClientThread()
        thread.start()
        thread.join(30)
        # After 30 seconds the thread should have finished.
        if thread.isAlive():
            thread.stop()
            self.assertTrue(False)
