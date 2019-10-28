import collections
import sys


ID, FORENAME, MIDDLENAME, SURNAME, DEPARTMENT = range(5)

User = collections.namedtuple("Users", "username forename middlename surname id")


def main():
    if len(sys.argv) == 1 or sys.argv[1] in {"-h", "--help"}:
        print("usage: {0} <file>...".format(sys.argv[0]))
        sys.exit()

    usernames = set()
    users = {}
    for filename in sys.argv[1:]:
        with open(filename, encoding="utf-8") as file:
            for line in file:
                line = line.rstrip()  # removing all trailing whitespace characters
                if line:
                    process_line(line, usernames, users)
    print_users(users)


def key_for(user):
    return user.surname.lower(), user.forename.lower(), user.id


def process_line(line, usernames, users):
    fields = line.split(":")
    username = generate_username(fields, usernames)
    user = User(username, fields[FORENAME], fields[MIDDLENAME], fields[SURNAME], fields[ID])
    users[key_for(user)] = user


def generate_username(fields, usernames):
    username = ((fields[FORENAME][0] + fields[MIDDLENAME][:1] +
                 fields[SURNAME]).replace("-", "").replace("'", ""))
    username = original_name = username[:8].lower()
    count = 1
    while username in usernames:
        username = "{0}{1}".format(original_name, count)
        count += 1
    usernames.add(username)
    return username


def format_user(user, name_width, username_width):
    initial = ""
    if user.middlename:
        initial = " " + user.middlename[0]
    name = "{0.surname}, {0.forename}{1}".format(user, initial)
    if len(name) > name_width:
        name = name[:name_width - 1] + "…"
    return "{0:<{nw}} ({1.id:4}) {1.username:{uw}}".format(name, user, nw=name_width, uw=username_width)


def print_users(users):
    name_width = 17
    username_width = 9

    header_fields = "{0:<{nw}} {1:^6} {2:{uw}}".format("Name", "ID", "Username", nw=name_width, uw=username_width)
    header_hyphens = "{0:-<{nw}} {0:-<6} {0:-<{uw}}".format("", nw=name_width, uw=username_width)
    header = f"{header_fields} {header_fields}\n{header_hyphens} {header_hyphens}"

    sorted_list = sorted(users)

    lines_per_page = 64
    index = 0
    while index < len(sorted_list):
        line = 0
        print(header)
        while line < lines_per_page and index < len(sorted_list):
            entry = format_user(users[sorted_list[index]], name_width, username_width)
            if index + 1 < len(sorted_list):
                entry += " " + format_user(users[sorted_list[index + 1]], name_width, username_width)
            print(entry)
            index += 2
            line += 1
        print("\f")


main()
