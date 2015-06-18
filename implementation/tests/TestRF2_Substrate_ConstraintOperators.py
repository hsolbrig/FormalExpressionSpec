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
        self.assertEqual({418171008, 42640003, 72048003, 58997001, 85189001, 67365005, 26826005, 235770006, 32084004,
                           9124008, 235769005, 25598004, 50846009, 8744003, 196781001, 28845006, 64994000, 266439004,
                           6503008, 51036000, 286967008, 5596004, 64252005, 151000160106, 123601005, 91313006, 4998000,
                           84534001, 28358004, 698294004, 95547004}, set(descendants_of(Sctids(74400008))))
        self.assertEqual({418171008, 42640003, 72048003, 58997001, 85189001, 67365005, 26826005, 235770006, 32084004,
                           9124008, 235769005, 25598004, 50846009, 8744003, 196781001, 28845006, 64994000, 266439004,
                           6503008, 51036000, 286967008, 5596004, 64252005, 151000160106, 123601005, 91313006, 4998000,
                           84534001, 28358004, 698294004, 95547004, 74400008}, set(descendantsOrSelf_of(Sctids(74400008))))

    def test_ancestors(self):
        self.assertEqual({362965005, 118234003, 249562008, 84410009, 123946008, 373407002, 386618008, 85919009,
                          118436003, 302292003, 118948005, 249561001, 386617003, 128121009, 53619000, 18526009,
                          300307005, 119523007, 302168000, 363171009, 76712006, 609624008, 609618002, 363170005,
                          128999004, 64572001, 404684003, 119292006, 301857004, 363169009, 128139000, 609627001,
                          138875005, 406123005, 79787007}, set(ancestors_of(Sctids(74400008))))
        self.assertEqual({362965005, 118234003, 249562008, 84410009, 123946008, 373407002, 386618008, 85919009,
                          118436003, 302292003, 118948005, 249561001, 386617003, 128121009, 53619000, 18526009,
                          300307005, 119523007, 302168000, 363171009, 76712006, 609624008, 609618002, 363170005,
                          128999004, 64572001, 404684003, 119292006, 301857004, 363169009, 128139000, 609627001,
                          138875005, 406123005, 79787007, 74400008}, set(ancestorsOrSelf_of(Sctids(74400008))))

    def test_simple_conjunction_1(self):

        # < 19829001 |disorder of lung| AND < 301867009 |edema of trunk|
        dol = descendants_of(Sctids(19829001))
        sdol = set(dol)
        self.assertEqual(len(sdol), len(dol))
        self.assertEqual(944, len(sdol))

        eot = descendants_of(Sctids(301867009))
        seot = set(eot)
        self.assertEqual(len(seot), len(eot))
        self.assertEqual(55, len(seot))

        e = set(dol & eot)
        se = sdol & seot
        self.assertEqual(se, e)
        self.assertEqual({233707008, 698640000, 233712009, 162970000, 700458001, 233706004, 19242006, 46847001,
                          233711002, 233705000, 196153002, 233710001, 698638005, 360371003, 196152007, 40541001,
                          95437004, 233709006, 276637009, 196151000, 89687005, 10519008, 405276000, 233708003,
                          11468004, 61233003, 67782005}, se)

if __name__ == '__main__':
    unittest.main()
