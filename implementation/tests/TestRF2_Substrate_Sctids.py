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

from ECLparser.rf2_substrate.RF2_Substrate_Sctids import *


class RF2_SubstrateTestCase(unittest.TestCase):
    def setUp(self):
        parser = argparse.ArgumentParser(description="Set up RF2 DB parameters and optionally create a database")
        parser.add_argument('configfile', help="Configuration file location")
        opts = parser.parse_args(['settings.conf'])
        rf2_values.set_configfile(opts.configfile, override=True)
        self.c = Sctids()

    def test_constructors(self):
        self.assertEqual("SELECT id FROM concept_ss WHERE active=1  AND locked = 0", self.c.as_sql())
        self.assertEqual("SELECT id FROM concept_ss WHERE active=1  AND locked = 0 AND (id IN (7440008))",
                         Sctids(7440008).as_sql())
        self.assertEqual("SELECT id FROM concept_ss WHERE active=1  AND locked = 0 AND (id IN (56,74400008))",
                         Sctids({74400008, 56}).as_sql())
        self.assertEqual("SELECT id FROM concept_ss WHERE active=1  AND locked = 0 AND (id IN (74400008,56))",
                         Sctids([74400008, 56]).as_sql())
        self.assertEqual("SELECT id FROM concept_ss WHERE active=1  AND locked = 0 AND (id IN (74400008))",
                         Sctids(Sctids(74400008)).as_sql())
        self.assertEqual("SELECT id FROM concept_ss WHERE active=1  AND locked = 0 AND (id IN (74400008))",
                         Sctids(Sctids(74400008)).as_sql())
        self.assertEqual("SELECT id FROM concept_ss WHERE active=1  AND locked = 0 AND (id < 10000)",
                         Sctids('id < 10000').as_sql())
        self.assertEqual("SELECT id FROM concept_ss WHERE active=1  AND locked = 0 AND (id IN (id < 1000,id > 10))",
                         Sctids(['id < 1000', 'id > 10']).as_sql())

    def test_len(self):
        cl = len(self.c)
        self.assertTrue(cl > 313014)        # Count as of 20150131
        self.assertEqual(cl, len(self.c))
        self.assertEqual(1, len(Sctids(74400008)))
        self.assertEqual(0, len(Sctids(56)))
        self.assertEqual(1, len(Sctids({74400008, 74400008})))
        self.assertEqual(1, len(Sctids([74400008, 74400008])))
        self.assertEqual(2, len(Sctids({74400008, 101009})))
        self.assertEqual({101009, 102002, 103007, 104001, 106004, 107008, 108003, 109006, 110001, 111002, 112009,
                          113004, 114005, 115006, 116007, 117003, 118008, 119000, 120006, 121005},
                         {v for _, v in zip(range(20), self.c)})

    def test_subsumption(self):
        self.assertTrue(self.c > Sctids({74400008}))
        self.assertFalse(Sctids(74400008) > Sctids({74400008, 101009}))
        d = Sctids((74400008, 101009))
        self.assertTrue(self.c > d)
        d = Sctids((74400008, 17))
        self.assertTrue(self.c > d)          # Interesting case -- 17 isn't in the list
        self.assertFalse(d > self.c)
        self.assertFalse(d >= self.c)
        self.assertFalse(self.c <= d)
        self.assertTrue(self.c >= self.c)
        self.assertTrue(self.c == self.c)
        self.assertFalse(self.c == d)

        self.assertTrue(74400008 in self.c)
        self.assertFalse(56 in self.c)

    def test_and(self):
        x = self.c & Sctids({74400008, 56, 101009})
        self.assertEqual("SELECT DISTINCT and_sctid1.id FROM (SELECT id FROM concept_ss WHERE active=1  AND locked = 0)"
                         " AS and_sctid1 JOIN (SELECT id FROM concept_ss WHERE active=1  AND locked = 0 AND "
                         "(id IN (56,101009,74400008))) AS and_sctid2 ON and_sctid1.id = and_sctid2.id", x.as_sql())
        self.assertEqual(2, len(x))
        self.assertEqual({74400008, 101009}, set(x))

    def test_or(self):
        x = Sctids({74400008, 56}) | Sctids(101009)
        # print(x.as_sql())
        self.assertEqual(2, len(x))
        self.assertEqual({74400008, 101009}, set(x))

    def test_minus(self):
        a = Sctids({101009, 102002, 103007, 104001, 106004, 107008, 108003})
        b = Sctids({107008, 108003, 109006, 110001, 111002, 112009, 113004, 114005, 115006, 116007, 117003})
        self.assertEqual({101009, 102002, 104001, 106004, 103007}, set(a - b))
        self.assertEqual(set(), set(b - b))
        self.assertEqual({74400008}, set(Sctids(74400008) - a))

    def test_xor(self):
        a = Sctids({101009, 102002, 103007, 104001, 106004, 107008, 108003})
        b = Sctids({107008, 108003, 109006, 110001, 111002, 112009, 113004, 114005, 115006, 116007, 117003})
        # c1 = a | b
        # print("C1=" + c1.as_sql())
        # print("R:" + str(set(c1)))
        # c2 = a & b
        # print("C2=" + c2.as_sql())
        # print("R:" + str(set(c2)))
        # c = a ^ b
        # print(c.as_sql())
        self.assertEqual(set(a) ^ set(b), set(a ^ b))

    def test_empty(self):
        a = Sctids({})
        b = Sctids({})
        self.assertEqual(a.union(b), a)
        self.assertEqual(a.intersect(b), a)


if __name__ == '__main__':
    unittest.main()
