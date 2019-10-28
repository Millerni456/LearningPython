import sys
import xml.sax.saxutils


def main():
    options = process_options()
    if options == (None, None):
        return
    print("using options: {0}".format(options))

    print_start()
    count = 0
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"
            print_line(line, color, options[0], options[1])
            count += 1
        except EOFError:
            break
    print_end()


def print_start():
    print("<table border='1'>")


def print_line(line, color, maxwidth, format):
    print("<tr bgcolor='{0}'>".format(color))
    fields = extract_fields(line)
    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",", "")
            try:
                x = float(number)
                print("<td align='right'>{0:{1}}</td>".format(round(x), format))
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                if len(field) <= maxwidth:
                    field = xml.sax.saxutils.escape(field)
                else:
                    field = "{0} ...".format(xml.sax.saxutils.escape(field[:maxwidth]))
                print("<td>{0}</td>".format(field))
    print("</tr>")


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for c in line:
        if c in "\"'":
            if quote is None:  # start of quoted string
                quote = c
            elif quote == c:  # end of quoted string
                quote = None
            else:
                field += c  # other quote inside quoted string
            continue
        if quote is None and c == ",":  # end of a field
            fields.append(field)
            field = ""
        else:
            field += c  # accumulating a field
    if field:
        fields.append(field)  # adding the last field
    return fields


def escape_html(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text


def print_end():
    print("</table>")


def process_options():
    maxwidth = 100
    format = ".0f"

    if len(sys.argv) > 1:
        if sys.argv[1] in ("-h", "--help"):
            print("usage: {0} [maxwidth=int] [format=str] < infile.csv > outfile.html".format(sys.argv[0]))
            return None, None
    try:
        for arg in sys.argv[1:]:
            keypair = arg.split("=")
            if keypair[0] == "maxwidth":
                maxwidth = int(keypair[1])
            elif keypair[0] == "format":
                format = keypair[1]
    except (ValueError, IndexError) as err:
        print(err)

    return maxwidth, format


main()
