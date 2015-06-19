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
import sys
import os
import re
import sqlparse
from antlr4.InputStream import InputStream
import textwrap


fixed_args=["ECL", "expressionConstraint",  "-v=ECLVisitor_implementation", "-i"]

def clean_sql(sql):
    return sqlparse.format(re.sub('-- .*?\n', '' , sql), reindent=True, keywordcase='upper')

def print_results(opts, input_,  rval, excpt=None):
        print("Result: %s" % ("Exception" if excpt else "Pass" if rval.inran('ok') else "Error"))
        print(input_)
        if not excpt and rval.inran('ok'):
            if len(rval.ok) < 100:
                print('\n'.join(textwrap.wrap(str(set(rval.ok)), 80)))
            else:
                print("Length=%s" % len(rval.ok))
            if opts.sql:
                print()
                print('=' * 60)
                print(clean_sql(rval.ok.as_sql()))
                print('=' * 60)



class CmdLine:
    def __iter__(self):
        return self

    def __next__(self):
        line = input()
        if not line:
            raise StopIteration
        return line

    @property
    def text(self):
        return '\n'.join([l for l in self])


def main(argv: list):
    _curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
    sys.path.append(os.path.join(_curdir, '../../ECLparser/parser'))
    sys.path.append(os.path.join(_curdir, '../../ECLparser/parser_impl'))
    sys.path.append(os.path.join(_curdir, '../..'))
    sys.path.append(os.path.join(_curdir, '../../../../../CTS2/rf2db'))
    sys.path.append(os.path.join(_curdir, '../../../../../CTS2/ConfigManager'))
    from ECLparser.scripts.TestRig_mod import build_argparser, parse_args, do_parse
    from ECLparser.rf2_substrate.RF2_Substrate import RF2_Substrate
    from ECLparser.interpreter import i_expressionConstraint
    ss = RF2_Substrate()
    parser_args = build_argparser()
    parser_args.add_argument("-i", "--interp", help="Interpret output", action="store_true")
    parser_args.add_argument("-s", "--sql", help="Output SQL", action="store_true")
    opts = parse_args(parser_args, fixed_args + argv)
    cmdline = CmdLine()
    try:
        while True:
            print("Expression:")
            input_ = cmdline.text
            result = do_parse(opts, InputStream(input_))
            if not result:
                print("Not a valid ECL expression")
            elif opts.interp:
                try:
                    print_results(opts, input_, i_expressionConstraint(ss, result))
                except Exception as e:
                    print_results(opts, input_, None, e)
                    print("EXCEPTION")
    except EOFError:
        pass


if __name__ == '__main__':
    main(sys.argv[1:])
