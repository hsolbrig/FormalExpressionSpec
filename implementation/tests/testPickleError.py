# -*- coding: utf-8 -*-
# Copyright (c) 2014, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
#     list of conditions and the following disclaimer.
#
#     Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions and the following disclaimer in the documentation
#     and/or other materials provided with the distribution.
#
#     Neither the name of the <ORGANIZATION> nor the names of its contributors
#     may be used to endorse or promote products derived from this software
#     without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, 
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

import unittest
import pickle
import sys

from ECLparser.z.z import FreeType, BasicType


class x2(BasicType):pass
x1 = FreeType(a=None)
class x3:

    class x3a:
        def __init__(self):
            self.stuff = "hi"

setattr(sys.modules[__name__], 'x3a', x3.x3a)
setattr(sys.modules[__name__], 'parser.z.z.FreeType.FreeTypeInstance', FreeType.FreeTypeInstance)
setattr(sys.modules[__name__], 'FreeTypeInstance', FreeType.FreeTypeInstance)


class TestPickle(unittest.TestCase):
    def test_1(self):

        y = x1(a=None)
        print(y)
        pickle.dump(x1, open("foo.pkl", 'wb'))

    def test_2(self):
        y = x2()
        print(y)
        pickle.dump(y, open("bar.pkl", 'wb'))

    def test_3(self):
        y = x3.x3a()
        print(y)
        pickle.dump(y, open("fee.pkl", 'wb'))



if __name__ == '__main__':
    unittest.main()
