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

import datetime
import logging

from jgtpyalgotrade import strategy
from jgtpyalgotrade import bar
from jgtpyalgotrade import logger
from jgtpyalgotrade.barfeed import membf


class TestBarFeed(membf.BarFeed):
    def barsHaveAdjClose(self):
        raise NotImplementedError()


class BacktestingStrategy(strategy.BacktestingStrategy):
    def __init__(self, barFeed, cash):
        strategy.BacktestingStrategy.__init__(self, barFeed, cash)

    def onBars(self, bars):
        self.info("bla")
        self.marketOrder("orcl", 1)


def main():
    bf = TestBarFeed(bar.Frequency.DAY)
    bars = [
        bar.BasicBar(datetime.datetime(2000, 1, 1), 10, 10, 10, 10, 10, 10, bar.Frequency.DAY),
        bar.BasicBar(datetime.datetime(2000, 1, 2), 10, 10, 10, 10, 10, 10, bar.Frequency.DAY),
        ]
    bf.addBarsFromSequence("orcl", bars)

    logger.getLogger().setLevel(logging.DEBUG)
    strat = BacktestingStrategy(bf, 1)
    strat.run()
