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
from antlr4 import FileStream
import textwrap

from ECLparser.rf2_substrate.RF2_Substrate import RF2_Substrate
from ECLparser.interpreter import i_expressionConstraint

ss = RF2_Substrate()

def clean_sql(sql):
    return sqlparse.format(re.sub('-- .*?\n', '' , sql), reindent=True, keywordcase='upper')

def print_results(opts, dirpath, fn, rval, excpt=None):
    if opts.outdir:
        with open(os.path.join(opts.outdir, fn + '.output'), 'w') as of:
            of.write("// Substrate: 20150131\n")
            of.write("// Timestamp: \n")
            of.write("// Result: %s\n\n" % ("Exception" if excpt else "Pass" if rval.inran('ok') else "Error"))
            of.write(open(os.path.join(dirpath, fn)).read())
            if not excpt and rval.inran('ok'):
                of.write("\n// Result: ")
                if len(rval.ok) < 100:
                    of.write('\n// '.join(textwrap.wrap(str(set(rval.ok)), 80)))
                of.write("\n//\n// Length=%s" % len(rval.ok))
                of.write("\n")
                if opts.sql:
                    of.write("\n// " + ('=' * 60) + '\n')
                    of.write('//' + clean_sql(rval.ok.as_sql()).replace('\n', '\n// '))
                    of.write("\n// " + ('=' * 60) + '\n')
    elif rval:
        if rval.inran('ok'):
            if opts.sql:
                print("=" * 80)
                print(rval.ok.as_sql())
                print("=" * 80)
            print("-" * 80)
            if len(rval.ok) == 0:
                print(">>>>> NO DATA <<<<<")
            else:
                print(set(rval.ok) if len(rval.ok) < 100 else ("%s items returned" % len(rval.ok)))
            print("-" * 80)
        else:
            print("ERROR")
    else:
        print(">" * 40 + "EXCEPTION!")
        print(open(os.path.join(dirpath, fn)).read())
        print("-" * 40)
        # print(rval.ok.as_sql())
        print(excpt)
        print(">" * 40)


def main(argv: list):
    _curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
    sys.path.append(os.path.join(_curdir, '../../ECLparser/parser'))
    sys.path.append(os.path.join(_curdir, '../../ECLparser/parser_impl'))
    sys.path.append(os.path.join(_curdir, '../..'))
    from ECLparser.scripts.TestRig_mod import build_argparser, parse_args, do_parse

    parser_args = build_argparser()
    parser_args.add_argument("-i", "--interp", help="Interpret output", action="store_true")
    parser_args.add_argument("-d", "--dir", help="Test directory", default='.')
    parser_args.add_argument("-f", "--file", help="File pattern to match")
    parser_args.add_argument("-o", "--outdir", help="Output directory for recording expected results")
    parser_args.add_argument("-s", "--sql", help="Output SQL", action="store_true")
    opts = parse_args(parser_args, argv)
    nviewed = nfailed = nsuccess = nexceptions = 0
    for (dirpath, _, filenames) in os.walk(opts.dir):
        for fn in filenames:
            if not fn.startswith('.') and not fn.endswith('.output') and (not opts.file or fn.startswith(opts.file)):
                print("PARSING: " + fn)
                result = do_parse(opts, FileStream(os.path.join(dirpath, fn)))
                nviewed += 1
                if not result:
                    print("FAILED")
                    nfailed += 1
                elif opts.interp:
                    try:
                        print_results(opts, dirpath, fn, i_expressionConstraint(ss, result))
                        print("SUCCESS")
                        nsuccess += 1
                    except Exception as e:
                        print_results(opts, dirpath, fn, None, e)
                        print("EXCEPTION")
                        nexceptions += 1
    print("Parsed %s files:" % nviewed)
    print("\tSuccess: %s" % nsuccess)
    print("\tParse Failure: %s" % nfailed)
    print("\tEvaluation Failure: %s" % nexceptions)


if __name__ == '__main__':
    main(sys.argv[1:])
