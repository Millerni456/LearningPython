import sys

Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = ["  *  ",
       " **  ",
       "* *  ",
       "  *  ",
       "  *  ",
       "  *  ",
       "*****"]
Two = [" *** ",
       "*   *",
       "*  * ",
       "  *  ",
       " *   ",
       "*    ",
       "*****"]
Three = [" *** ",
         "*   *",
         "    *",
         "  ** ",
         "    *",
         "*   *",
         " *** "]
Four = ["   *  ",
        "  **  ",
        " * *  ",
        "*  *  ",
        "******",
        "   *  ",
        "   *  "]
Five = ["*****",
        "*    ",
        "*    ",
        "**** ",
        "    *",
        "*   *",
        " *** "]
Six = [" *** ",
       "*    ",
       "*    ",
       "**** ",
       "*   *",
       "*   *",
       " *** "]
Seven = ["*****",
         "    *",
         "   * ",
         "  *  ",
         " *   ",
         "*    ",
         "*    "]
Eight = [" *** ",
         "*   *",
         "*   *",
         " *** ",
         "*   *",
         "*   *",
         " *** "]
Nine = [" ****",
        "*   *",
        "*   *",
        " ****",
        "    *",
        "    *",
        "    *"]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

digits = None
try:
    digits = sys.argv[1]
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            for character in digit[row]:
                if character == "*":
                    character = str(number)
                line += character
            line += "  "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("usage: Exercise1.1.py <number>")
except ValueError as err:
    print(err, "in", digits)
