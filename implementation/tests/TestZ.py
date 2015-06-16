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

from ECLparser.z import *


class TestZTypes(unittest.TestCase):
    def test_builtins(self):
        # self.assertTrue(1 in Z)
        unity = Z(1)
        self.assertEqual("1", str(unity))
        self.assertEqual(1, unity)
        self.assertTrue(Z.has_member(unity))
        self.assertTrue(Z.has_member(-1))
        self.assertFalse(Z.has_member('abc'))
        self.assertFalse(Z.has_member(BasicType))
        self.assertFalse(Z.has_member(BasicType()))
        min_ = N(4)
        self.assertEqual("4", str(min_))
        self.assertEqual(4, min_)
        self.assertEqual(N_1(4), min_)
        self.assertTrue(Z.has_member(min_))
        self.assertTrue(N.has_member(min_))
        self.assertTrue(N_1.has_member(min_))
        self.assertTrue(Z.has_member(Z(-1)))
        self.assertFalse(N.has_member(Z(-1)))
        self.assertFalse(N_1.has_member(Z(0)))
        self.assertTrue(N_1.has_member(Z(1)))
        cat_count = N
        x = cat_count(17)
        self.assertEqual(x, 17)
        self.assertTrue(cat_count.has_member(x))

    def test_free_type(self):
        class color(BasicType): pass

        red = color()
        yellow = color()
        blue = color()
        self.assertTrue(color.has_member(red))
        self.assertFalse(color.has_member(N(1)))
        self.assertEqual(red, red)
        self.assertNotEqual(red, blue)


class TestTypes(unittest.TestCase):
    def test_z(self):
        x = Z(17)
        y = Z(-143)
        self.assertTrue(x == 17 and y == -143)
        with self.assertRaises(AssertionError):
            N(-1)

    def test_freetype(self):
        C = FreeType(t_int=int, t_str=str, t_unit=None)
        with self.assertRaises(AssertionError):
            C(t_real=0.0)
        x_c = C(t_int=17)
        self.assertTrue(x_c.inran('t_int'))
        self.assertFalse(x_c.inran('t_unit'))
        with self.assertRaises(AssertionError):
            x_c.inran('t_foo')
        y_c = C(t_int=17)
        self.assertEqual(x_c, y_c)
        z_c = C(t_str='foo')
        self.assertNotEqual(x_c, z_c)
        self.assertEqual(z_c.t_str, "foo")
        t_c = C(t_unit=None)
        self.assertTrue(t_c.inran('t_unit'))

    def test_nested_constructors(self):
        C = FreeType(t_int=int, t_str=str, t_unit=None)
        D = FreeType(c_int=int, c_c=C)
        y_c = C(t_int=17)
        x_d = D(c_c=y_c)
        self.assertEqual(x_d.c_c.t_int, 17)

    def test_freetype2(self):
        Degree = FreeType(status=range(0, 4))
        ba = Degree(status=0)
        msc = Degree(status=1)
        dphil = Degree(status=2)
        ma = Degree(status=3)

        def le_status(d1:Degree, d2:Degree):
            return d1.status <= d2.status

        self.assertTrue(le_status(dphil, ma))

    def test_seq(self):
        class FOO(BasicType): pass

        a = FOO()
        b = FOO()
        c = FOO()
        d = FOO()
        e = FOO()
        S = Seq(FOO)
        self.assertEqual(S(a, b, c, d, e), S(a, b, c).concat(S(d, e)))
        with self.assertRaises(AssertionError):
            S(a, b, (c, d))
        self.assertEqual(S((a, b, c, d, e)), S((a, b, c)).concat(S(d, e)))

    def test_filter(self):
        class FOO(BasicType): pass

        a = FOO()
        b = FOO()
        c = FOO()
        d = FOO()
        e = FOO()
        fs = Seq(FOO)(a, b, c, d, e, d, c, b, a).filter([a, d])
        gs = Seq(FOO)(a, d, d, a)
        self.assertEqual(fs, gs)
        self.assertEqual(Seq(FOO)(a, b, c, d, e, d, c, b, a).filter([a, d]), Seq(FOO)(a, d, d, a))

    def test_set(self):
        x = Set(int)
        x_i = x(1, 2, 3, 4, 3, 3, 0)
        # self.assertEqual({0, 1, 2, 3, 4}, x_i.v)

    def test_seq_n(self):
        x = Seq_1(int)
        x(1)
        with self.assertRaises(AssertionError):
            x()

        class Optional(Seq):
            maxlen = 1

        x = Optional(int)
        self.assertFalse(x(1).is_empty)
        self.assertTrue(x().is_empty)
        with self.assertRaises(AssertionError):
            x(1, 2)

    def test_cross_product(self):
        x = CrossProduct(int, str)
        x_1 = x(1, 'abc')
        self.assertEqual(1, x_1.first)
        self.assertEqual('abc', x_1.second)
        y = CrossProduct()('143', Seq(int)(1, 2, 3))
        self.assertEqual('143', y.first)
        self.assertEqual((1, 2, 3), y.second.v)
        z = CrossProduct(Seq(int), str)
        z_f = Seq(int)(1, 2, 3)
        z_v = z(z_f, 'abc')
        self.assertEqual((1, 2, 3), z_v.first.v)
        self.assertEqual('abc', z_v.second)

    def test_forward(self):
        x = Forward()
        x << CrossProduct(int, str)
        self.assertEqual((1, 'abc'), x(1, 'abc').v)
        y = Forward()
        y << CrossProduct(Seq(int), str)
        y_c = y(Seq(int)([1, 2, 3]), 'zzz')
        self.assertEqual((1, 2, 3), y_c.first.v)
        z = Forward()
        z << CrossProduct(Seq(z), Seq(z))
        z_1 = z(Seq(z)([]), Seq(z)([]))
        z_2 = z(Seq(z)([z_1, z_1]), Seq(z)())

    def test_instances(self):
        z1 = Z(3)
        z2 = Z(0)
        z3 = Z(-1)
        N1 = N(3)
        N2 = N(0)
        N_11 = N(1)
        self.assertTrue(Z.has_member(1))
        self.assertTrue(N.has_member(0))
        nums = Seq(Z)
        primes = nums([Z(2), Z(3), Z(5), Z(7)])
        self.assertTrue(nums.has_member(primes))


from ECLparser.datatypes import sctId, target, groupId, is_a, zero_group, unlimitedNat, many, Optional, cardinality, \
    reverseFlag, constraintOperator, attributeOperatorValue, attributeName, Sctids_or_Error


class TestSchema(unittest.TestCase):
    def test_1(self):
        Quad = Schema(lambda q: q.a != is_a or (q.g == 0 and q.t.inran('t_sctid')),
                      s=sctId, a=sctId, t=target, g=groupId)
        v = sctId(450828004)
        t = target(t_sctid=v)
        q1 = Quad(s=sctId(450828004), a=sctId(116680003), t=t, g=zero_group)
        with self.assertRaises(AssertionError):
            Quad(s=sctId(450828004), a=sctId(116680003), t=target(t_sctid=sctId(450828004)), g=groupId(1))
        with self.assertRaises(AssertionError):
            Quad(s=sctId(450828004), a=sctId(116680003), t=target(t_sctid=sctId(450828004)), g=groupId(1), l=1)
        self.assertTrue(q1.__eq__(q1))
        self.assertEqual(q1, q1)
        self.assertEqual(Quad(s=sctId(450828004), a=sctId(116680003), t=target(t_sctid=sctId(450828004)), g=zero_group),
                         q1)
        self.assertNotEqual(
            Quad(s=sctId(450829007), a=sctId(116680003), t=target(t_sctid=sctId(450828004)), g=zero_group), q1)
        self.assertNotEqual(1, q1)
        foo = Schema(v=int)
        self.assertNotEqual(foo(v=1), q1)

    def test_2(self):
        cardinality = z.Schema(min_=z.N, max_=unlimitedNat)
        # TODO: positional args not implemented
        # ztn = cardinality(0, many)
        ztn = cardinality(min_=0, max_=many)
        # TODO: This fails half the time because dictionaries aren't ordered
        # self.assertEqual("[min_=0, max_=many ⟨⟨ None ⟩⟩ ]", str(ztn))
        oto = cardinality(min_=1, max_=unlimitedNat(num=1))
        oc = Optional(cardinality)(cardinality(min_=1, max_=unlimitedNat(num=1)))
        print(oc)

    def test_3(self):
        attribute = Schema(card=Optional(cardinality), rf=Optional(reverseFlag),
                           attrOper=Optional(constraintOperator), name=attributeName, opValue=attributeOperatorValue)

    def test_opt_instance(self):
        def getNext(f, l):
            for e in l:
                if f(e):
                    return e
            return None

        a = sctId(15)
        a_1 = 15
        b = Optional(reverseFlag)
        c = Optional(cardinality)()
        one = unlimitedNat(num=1)
        d = cardinality(min_=1, max_=one)
        e = Optional(cardinality)(cardinality(min_=1, max_=unlimitedNat(num=1)))
        getNext(lambda e: Optional(cardinality).has_member(e), [a, a_1, b, c, d, e])


class Test_type_issue(unittest.TestCase):
    def test_1(self):
        conceptId = N
        conceptReference = z.CrossProduct(conceptId, Optional(N))
        crOrWildCard = z.FreeType(cr=conceptReference, wc=None)
        focusConcept = z.FreeType(focusConcept_m=crOrWildCard, focusConcept_c=crOrWildCard)
        compoundExpressionConstraint = Forward()
        simpleExpressionConstraint = Forward()
        unrefinedExpressionConstraint = z.FreeType(unrefined_compound=compoundExpressionConstraint,
                                                   unrefined_simple=simpleExpressionConstraint)
        sec = N
        eec = z.CrossProduct(sec, sec)
        dec = z.CrossProduct(sec, z.Seq_1(sec))

        simpleExpressionConstraint << z.CrossProduct(Optional(constraintOperator), focusConcept)
        compoundExpressionConstraint << z.FreeType(compound_disj=dec, compound_excl=eec,
                                                   compound_nested=compoundExpressionConstraint)
        zz = conceptReference(conceptId(15), None)
        zzz = crOrWildCard(cr=zz)
        fc = focusConcept(focusConcept_c=zzz)
        oco = Optional(constraintOperator)()
        val = simpleExpressionConstraint(oco, fc)
        z._MetaType.is_instance(val, eec)
        self.assertFalse(z._MetaType.is_instance(val, eec))
        # This fails randomly, because the order of unrefined_compound / unrefined_simple in the definition.
        # If we test simple first, we are fine.  compound first results in an error
        rslt = unrefinedExpressionConstraint.assign(val)
        print(rslt)

    def test_2(self):
        sctidRef = z.FreeType(a=sctId)
        x = sctidRef(a=sctId(15))
        self.assertTrue(z._MetaType.is_instance(x, sctidRef))


class Test_Z_Ref_Card(unittest.TestCase):
    def test_basic_type(self):
        class NAME(BasicType): pass

        class DATE(BasicType): pass

        y = NAME()
        z = DATE()
        self.assertFalse(y == z)
        self.assertTrue(NAME.has_member(y))
        self.assertFalse(NAME.has_member(z))

        class CHAR(BasicType): pass

        DOC = Seq(CHAR)

        Point = Schema(x=Z, y=Z)

        Ans = FreeType(ok=Z, error=None)


class Test_Seq_Print_error(unittest.TestCase):
    def test_1(self):
        t1 = Seq(N)()
        t2 = Seq(N)((1,))
        t3 = Seq(N)((1, 2))
        with self.assertRaises(AssertionError):
            print(t1.head)          # Empty classes have no head
        with self.assertRaises(AssertionError):
            print(t1.tail)          # Empty classes have no tail
        self.assertEqual(1, t2.head)
        self.assertTrue(t2.tail.is_empty)
        self.assertEqual("∅", str(t2.tail))
        self.assertEqual(1, t3.head)
        self.assertEqual("⟨ 2⟩ ", str(t3.tail))
        self.assertEqual("∅", str(t3.tail.tail))


class Test_Membership(unittest.TestCase):
    def test_member(self):
        t1 = Set(N)((1, 2, 3))
        self.assertTrue(1 in t1)
        self.assertFalse(4 in t1)
        self.assertTrue(N(1) in t1)
        self.assertFalse(BasicType in t1)

        t2 = Seq(N)([1, 2, 3, 1])
        self.assertTrue(1 in t2)

class Test_Unhashable(unittest.TestCase):
    def test_1(self):
        # You can't have a set that contains unhashable contents
        t1 = Set(FreeType(a=None))(FreeType(a=None)(a=None))

class Test_rval(unittest.TestCase):
    def test_1(self):
        # This situation currently doesn't work.  We tried some setters in the FreeTypeInstance, but
        # it got to be a mess, so we're going to require constructors with args for the time being
        # rval = Sctids_or_Error()
        # rval.ok = Set(sctId)(sctId(36))
        # self.assertTrue(rval.inran('ok'))
        # print(str(rval))
        self.assertTrue(True)

class Test_print_fwd(unittest.TestCase):
    compoundExpressionConstraint = Forward()
    compoundExpressionConstraint << z.FreeType(compound_conj=N,
                                               compound_nested=compoundExpressionConstraint)
    x = compoundExpressionConstraint(compound_conj=1)
    y = compoundExpressionConstraint(compound_nested=x)
    str(y)


if __name__ == '__main__':
    unittest.main()
