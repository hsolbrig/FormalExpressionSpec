# -*- coding: utf-8 -*-
# Copyright (c) 2015, Mayo Clinic
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

from rf2db.db.RF2FileCommon import rf2_values
import argparse

from ECLparser.rf2_substrate.RF2_Substrate_ConstraintOperators import *


class RF2_TransitiveTestCase(unittest.TestCase):
    def setUp(self):
        parser = argparse.ArgumentParser(description="Set up RF2 DB parameters and optionally create a database")
        parser.add_argument('configfile', help="Configuration file location")
        opts = parser.parse_args(['settings.conf'])
        rf2_values.set_configfile(opts.configfile)
        self.c = Sctids()

    def test_descendants(self):
        print(set(descendants(Sctids(74400008))))

    def test_simple_conjunction_1(self):
        # < 19829001 |disorder of lung| AND < 301867009 |edema of trunk|
        e = descendants(Sctids(19829001)) & descendants(Sctids(301867009))
        print(e.as_sql())
        print(set(descendants(Sctids(19829001)) & descendants(Sctids(301867009))))

if __name__ == '__main__':
    unittest.main()
