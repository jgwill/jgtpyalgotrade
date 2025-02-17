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

from jgtpyalgotrade import technical
from jgtpyalgotrade import utils


class RatioEventWindow(technical.EventWindow):
    def __init__(self):
        super(RatioEventWindow, self).__init__(2)

    def getValue(self):
        ret = None
        if self.windowFull():
            prev = self.getValues()[0]
            actual = self.getValues()[-1]
            ret = utils.get_change_percentage(actual, prev)
        return ret


# Calculates the ratio between a value and the previous one.
# The ratio can't be calculated if a previous value is 0.
class Ratio(technical.EventBasedFilter):
    def __init__(self, dataSeries, maxLen=None):
        super(Ratio, self).__init__(dataSeries, RatioEventWindow(), maxLen)
