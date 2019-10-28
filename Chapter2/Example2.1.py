import sys
import unicodedata


def print_unicode_table(word):
    print("decimal   hex   chr  {0:^40}".format("name"))
    print("-------  -----  ---  {0}".format("-" * 40))

    code = ord(" ")
    end = sys.maxunicode

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        if word is None or word in name.lower():
            print("{0:7}  {0:5X}  {0:^3c}  {1}".format(code, name.title()))

        code += 1

        # Skip the surrogate pair code points as they are unsupported in UTF-8.
        if code == 0xD800:
            code = 0xE000


word = None
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string]".format(sys.argv[0]))
        word = 0
    else:
        word = sys.argv[1].lower()
if word != 0:
    print_unicode_table(word)