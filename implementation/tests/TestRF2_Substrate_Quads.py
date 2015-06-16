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

from ECLparser.rf2_substrate.RF2_Substrate_Quads import *
from ECLparser.rf2_substrate.RF2_Substrate_Sctids import Sctids


class RF2_SubstrateTestCase(unittest.TestCase):
    def setUp(self):
        parser = argparse.ArgumentParser(description="Set up RF2 DB parameters and optionally create a database")
        parser.add_argument('configfile', help="Configuration file location")
        opts = parser.parse_args(['settings.conf'])
        rf2_values.set_configfile(opts.configfile)

    def _test_result(self, t1, ngroups):
        # print(t1.as_sql())
        # print('\n'.join(str(e) for e in t1))
        self.assertEqual(ngroups, len(t1))

    def test_constructors(self):
        t1 = Quads(rf=True, atts=Sctids(118170007), eq=True, ecv=Sctids({116154003, 32712000}))
        self._test_result(t1, 10)
        t1 = Quads(rf=False, atts=Sctids(118170007), eq=True, ecv=Sctids({119306004, 258647001, 431776009}))
        self._test_result(t1, 3)
        t1 = Quads(rf=True, atts=Sctids(116680003), eq=False, ecv=Sctids({116154003, 32712000}))
        self._test_result(t1, 64)
        t1 = Quads(rf=True, atts=Sctids({116680003, 363699004}), eq=False, ecv=Sctids({116154003, 32712000}))
        self._test_result(t1, 19)
        t1 = Quads()
        self.assertTrue(930350 < len(t1))

    def test_to_sctids(self):
        t1 = Quads(rf=True, atts=Sctids(116680003), eq=False, ecv=Sctids({116154003, 32712000}))
        self._test_result(t1, 64)
        c1 = t1.to_sctids()
        self.assertEqual(
            "SELECT id FROM concept_ss WHERE active=1  AND locked = 0 AND "
            "(id IN (SELECT r.sourceId FROM (SELECT id, sourceId, typeId, destinationId, relationshipGroup "
            "FROM relationship_ss WHERE typeId NOT IN (SELECT id FROM concept_ss WHERE active=1  "
            "AND locked = 0 AND (id IN (116680003))) AND destinationId IN "
            "(SELECT id FROM concept_ss WHERE active=1  AND locked = 0 AND "
            "(id IN (32712000,116154003))) AND active=1 AND locked=0) AS r) )", c1.as_sql())
        self.assertEqual({119306004, 258647001, 39668000, 225115005, 241026003, 241027007, 241029005, 427219009,
                          427479001, 315028004, 47956003, 241030000, 241028002, 433043005, 241031001, 44267002,
                          287727009, 179005009, 179006005, 432875004, 304846008, 50686003, 406155005, 431842009,
                          230827000, 230819009, 230831006, 73914006, 24959006, 51748005, 315031003, 56821003,
                          432273003, 434289001, 433307009, 433767008, 55628002, 40148000, 432105003, 432391006,
                          431701003, 433241004, 431618007, 432871008, 12682005, 431845006, 440549000, 440104006,
                          439781002, 447388001, 431776009, 432243007, 698956007, 119299002, 122561005, 122584003,
                          122588000, 122590004, 122583009, 440493002}, set(c1))

