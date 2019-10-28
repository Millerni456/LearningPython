import sys
import unicodedata


def print_unicode_table(words):
    print("decimal   hex   chr  {0:^40}".format("name"))
    print("-------  -----  ---  {0}".format("-" * 40))

    code = ord(" ")
    end = sys.maxunicode

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        should_print = True
        for word in words:
            if word not in name.lower():
                should_print = False
                break
        if should_print:
            print("{0:7}  {0:5X}  {0:^3c}  {1}".format(code, name.title()))

        code += 1

        # Skip the surrogate pair code points as they are unsupported in UTF-8.
        if code == 0xD800:
            code = 0xE000


words = []
if len(sys.argv) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print("usage: {0} [string1 [string2 [... stringN]]]".format(sys.argv[0]))
        words = None
    else:
        words = []
        for word in sys.argv[1:]:
            words.append(word.lower())
if words is not None:
    print_unicode_table(words)
