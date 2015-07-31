# -*- coding: utf-8 -*-
# Copyright (c) 2015, Mayo Clinic
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
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
import argparse
import os
import sys
import pickle

from antlr4 import *
from antlr4.InputStream import InputStream
from antlr4.error import DiagnosticErrorListener
from antlr4.atn.PredictionMode import PredictionMode

_curdir = os.path.join(os.getcwd(), os.path.dirname(__file__))
sys.path.append(os.path.join(_curdir, '..'))


# If the lexer start rule is 'tokens' this is strictly a lexer test.  THere is no associated parser
LEXER_START_RULE_NAME = 'tokens'


def build_argparser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run ANTLR4 Python TestRig")
    parser.add_argument("grammar", help="Grammar name")
    parser.add_argument("startRule", help="Start rule name")
    parser.add_argument("-t", "--tokens", help="Display parse tokens", action="store_true")
    parser.add_argument("-tr", "--tree", help="Display parse tree", action="store_true")
    parser.add_argument("-g", "--gui", help="Display GUI interface", action="store_true")
    # parser.add_argument("-p", "--psfile", help="Postscript file output", type=str)
    parser.add_argument("-e", "--encoding", help="Input file encoding", type=str)
    parser.add_argument("-w", "--walker", help="Listener to walk", type=str)
    parser.add_argument("-v", "--visitor", help="Visitor to visit", type=str)
    parser.add_argument("--trace", help="Trace", action="store_true")
    parser.add_argument("--diagnostics", help="Disgnostics", action="store_true")
    parser.add_argument("--SLL", help="?", action="store_true")
    parser.add_argument("-p", "--pickle", help="Pickle the resulting output into file", type=str)
    return parser


def parse_args(argparser: argparse.ArgumentParser, args: list) -> argparse.Namespace:
    """ Parse the input arguments
    :return: Parsed input arguments
    """
    parsed_args = argparser.parse_args(args)
    parsed_args.lexerOnly = parsed_args.startRule == LEXER_START_RULE_NAME
    parsed_args.grammar_title = parsed_args.grammar[0].upper() + parsed_args.grammar[1:]
    parsed_args.psfile = None
    return parsed_args


class StdInputStream(InputStream):
    """ Create an inputstream out of stdin
    """
    def __init__(self):
        InputStream.__init__(self, sys.stdin.read())


def get_object(name):
    lexer_module = __import__(name, fromlist=[name])
    return getattr(lexer_module, name)


def get_lexer(args: argparse.Namespace, infile: InputStream) -> Lexer:
    """ Build a lexer from the inputstream
    :param args: input arguments
    :param infile: input stream
    :return:
    """
    return get_object(args.grammar_title + ('' if args.lexerOnly else 'Lexer'))(infile)


def get_parser(args: argparse.Namespace, tokens: CommonTokenStream) -> Parser:
    """ Build a parser
    :param args:
    :return:
    """
    return (get_object(args.grammar_title + 'Parser')(tokens)) if not args.lexerOnly else None


def do_parse(opts: argparse.Namespace, infile: InputStream):

    tokens = CommonTokenStream(get_lexer(opts, infile))
    tokens.fill()
    if opts.tokens:
        for t in tokens.getTokens(0, len(tokens.tokens) - 1):
            print(t)

    parser = get_parser(opts, tokens)
    if not parser:
        sys.exit(1)

    if opts.diagnostics:
        parser.addErrorListener(DiagnosticErrorListener)
        parser.predictionMode = PredictionMode.LL_EXACT_AMBIG_DETECTION

    if opts.tree or opts.gui or opts.psfile:
        parser.buildParseTrees = True

    if opts.SLL:
        parser.predictionMode = PredictionMode.SLL

    # parser.setTrace(opts.trace)
    # TODO: Trace doesn't work - it has a big programming error
    if opts.trace:
        print("Trace is not implemented correctly")

    tree = getattr(parser, opts.startRule)()
    result = None
    if opts.walker:
        walker = get_object(opts.walker)()
        result = ParseTreeWalker().walk(walker, tree)

    if opts.visitor:
        visitor = get_object(opts.visitor)()
        result = visitor.visit(tree)

    if opts.tree:
        print(tree.toStringTree())
    if opts.gui:
        # TODO: see whether this can be implemented
        print("gui function is not implemented")
    # if opts.psfile:
    #     # TODO: save is not implemented
    #     # tree.save(parser, opts.psfile)
    #     print("postscript save function is not implemented")
    if opts.pickle and result:
        pickle.dump(result, open(opts.pickle, 'wb'), fix_imports=True)
        print("Results pickled into %s" % opts.pickle)

    return result


def main(argv: list):
    sys.path.append(os.path.join(_curdir, '..'))
    sys.path.append(os.path.join(_curdir, '../parser/parser'))

    parser_args = build_argparser()
    parser_args.add_argument("infile", help="Input file to parse. If absent, parse stdin", nargs='?')

    opts = parse_args(parser_args, argv)

    result = do_parse(opts, FileStream(opts.infile) if opts.infile else StdInputStream())
    if result:
        print(result)

if __name__ == '__main__':
    main(sys.argv[1:])
