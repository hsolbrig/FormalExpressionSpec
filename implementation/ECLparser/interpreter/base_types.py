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
from collections import Sized

from ECLparser.z.z import CrossProduct, Seq, Set, N
from ECLparser.datatypes import zero_group, sctId, Sctids_or_Error, unlimitedNat, many, \
    Quads_or_Error, Quad, direction, uniqueGroupId, sctIdGroups_or_Error
from ECLparser.test_substrate.substrate import Substrate

def quadGroup(q: Quad) -> uniqueGroupId:
    if q.g != zero_group:
        return uniqueGroupId(ug=q.g)
    else:
        return uniqueGroupId(zg=q)


# 5.2 Result transformations
def result_sctids(r: Sctids_or_Error) -> Seq(sctId):
    if r.inran('error'):
        return Seq(sctId)()
    else:
        return r.ok


def quads_for(q: Quads_or_Error) -> Seq(Quad):
    return Seq(Quad)() if q.inran('qerror') else q.quad_value.first


def quad_direction(q: Quads_or_Error) -> direction:
    return q.quad_value.second


def first_error(x: Seq(Sctids_or_Error)) -> Sctids_or_Error:
    assert any([e.inran('error') for e in x.v]), "Must be at least one error entry"
    for e in x.v:
        if e.inran('error'):
            return e
    return None         # can't happen


def gfirst_error(x: Seq(sctIdGroups_or_Error)) -> sctIdGroups_or_Error:
    assert any([e.inran('gerror') for e in x.v]), "Must be at least one error entry"
    for e in x.v:
        if e.inran('gerror'):
            return e
    return None


def union(x: Sctids_or_Error, y: Sctids_or_Error) -> Sctids_or_Error:
    if x.inran('error') or y.inran('error'):
        return first_error(Seq(Sctids_or_Error)(x, y))
    # return Sctids_or_Error(ok=x.ok.union(y.ok))
    return Sctids_or_Error(ok=x.ok | y.ok)


def intersect(x: Sctids_or_Error, y: Sctids_or_Error) -> Sctids_or_Error:
    if x.inran('error') or y.inran('error'):
        return first_error(Seq(Sctids_or_Error)(x, y))
    return Sctids_or_Error(ok=x.ok.intersect(y.ok))

def minus(x: Sctids_or_Error, y: Sctids_or_Error) -> Sctids_or_Error:
    if x.inran('error') or y.inran('error'):
        return first_error(Seq(Sctids_or_Error)(x, y))
    # return Sctids_or_Error(ok=x.ok.difference(y.ok))
    return Sctids_or_Error(ok=x.ok - y.ok)


def bigunion(x: Seq(Sctids_or_Error)) -> Sctids_or_Error:
    if any([e.inran('error') for e in x]):
        return first_error(x)
    return Set.SetInstance.bigcup(Set(sctId), [e.ok for e in x])


def bigintersect(x: Seq(Sctids_or_Error)) -> Sctids_or_Error:
    if any([e.inran('error') for e in x]):
        return first_error(x)
    return Set.SetInstance.bigcap(Set(sctId), [e.ok for e in x])


def gunion(x: sctIdGroups_or_Error, y: sctIdGroups_or_Error) -> sctIdGroups_or_Error:
    if x.inran('error') or y.inran('error'):
        return first_error(Seq(Sctids_or_Error)(x, y))
    return x.group_value.union(y.group_value)


def gintersect(x: sctIdGroups_or_Error, y: sctIdGroups_or_Error) -> sctIdGroups_or_Error:
    if x.inran('gerror') or y.inran('gerror'):
        return gfirst_error(Seq(sctIdGroups_or_Error)(x, y))
    return x.group_value.intersect(y.group_value)


def gminus(x: Sctids_or_Error, y: Sctids_or_Error) -> Sctids_or_Error:
    if x.inran('gerror') or y.inran('gerror'):
        return gfirst_error(Seq(sctIdGroups_or_Error)(x, y))
    return x.group_value.intersect(y.group_value)


# B Generic cardinality evaluation
# NOTE: return type is different than in spec
def evalCardinality(min_: N, max_: unlimitedNat, t: Sized) -> bool:
    return len(t) >= min_ and (max_ == many or len(t) <= max_)


# C Generic sequence function
def applyToSequence(ss: Substrate, f, op, seq_e) -> Sctids_or_Error:
    return op(f(ss, seq_e.first), f(ss, seq_e.head.second)) if seq_e.second.tail.is_empty else \
           op(f(ss, seq_e.first), applyToSequence(ss, f, op, CrossProduct()(seq_e.second.head, seq_e.second.tail)))