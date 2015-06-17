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

from ECLparser.rf2_substrate.RF2_Substrate_SctidGroups import *
from ECLparser.rf2_substrate.RF2_Substrate_Quads import Quads


class RF2_SubstrateSctidGroupTestCase(unittest.TestCase):
    def setUp(self):
        parser = argparse.ArgumentParser(description="Set up RF2 DB parameters and optionally create a database")
        parser.add_argument('configfile', help="Configuration file location")
        opts = parser.parse_args(['settings.conf'])
        rf2_values.set_configfile(opts.configfile)

    def _test_result(self, t1, nentries):
        # print(t1.as_sql())
        # print('\n'.join(str(e) for e in t1))
        self.assertEqual(nentries, len(t1))

    def test_constructors(self):
        q1 = Quads(rf=False, atts=Sctids(118170007), eq=True, ecv=Sctids({116154003, 32712000}))
        t1 = SctidGroups(q1)
        self._test_result(t1, 10)

    def test_to_sctids(self):
        q1 = Quads(rf=False, atts=Sctids(116680003), eq=False, ecv=Sctids({116154003, 32712000}))
        t1 = SctidGroups(q1)
        self._test_result(t1, 64)
        c1 = t1.to_sctids()
        self._test_result(c1, 60)


