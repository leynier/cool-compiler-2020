from sys import argv
from cool_lang.lexer import COOL_LEXER
from cool_lang.parser import COOL_PARSER


INPUT_FILE = argv[1]
OUTPUT_FILE = argv[2]

code = open(INPUT_FILE, encoding="utf8").read()

clexer = COOL_LEXER()
if not clexer.tokenize(code):
    for error in clexer.errors:
        print(error)
    exit(1)

cparser = COOL_PARSER()
if not cparser.parse(clexer.result):
    for error in cparser.errors:
        print(error)
    exit(1)
