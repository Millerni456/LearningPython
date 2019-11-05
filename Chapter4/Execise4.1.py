import os
import sys


def get_path():
    path = "."
    if len(sys.argv) > 1:
        if sys.argv[1] in {'-h', '--help'}:
            print(f"usage: {sys.argv[0]} [target_directory]")
            sys.exit()
        else:
            path = sys.argv[1]

    return path


def prompt_new_file():
    new_file = input("Enter a file name to create a .lst file: ")
    if not new_file.endswith(".lst"):
        new_file += ".lst"
    print(f"Creating file with the name: \"{new_file}\"\n")
    fh = None
    try:
        fh = open(new_file, mode="w")
    except EnvironmentError as e:
        print(f"Failed to create new file {new_file}: {e}\n")
    finally:
        fh.close()


def main():
    target_directory = get_path()

    while True:
        # Create a list of files in the current directory ending with .lst
        print(f"*.lst files at the path: \"{target_directory}\":")
        lst_files = [file for file in os.listdir(target_directory) if file.endswith(".lst")]

        if lst_files:
            for lino, file in enumerate(lst_files, 1):
                print(f"\t{lino}: {file}")
            print()

            response = input("Select a file number to edit (0 to add a new file): ")
            try:
                fileno = int(response)

                if fileno == 0:
                    prompt_new_file()
                else:
                    manage_file(lst_files[fileno - 1])
            except ValueError as e:
                print(f"Invalid file number: {response}.")
        else:
            print("\t- (None)\n")
            prompt_new_file()


def manage_file(filename):
    print(f"Chosen filename: \"{filename}\"")

    original_lines = load(filename)
    lines = original_lines.copy()

    is_managing = True
    while is_managing:
        if lines:
            for lino, line in enumerate(lines, 1):
                print(f"\t{lino}: {line.strip()}")

            response = input("[A]dd [D]elete [S]ave [Q]uit [a]: ").lower()
            if not response:
                response = "a"

            if response == "a":
                add_string(lines)
            elif response == "d":
                delete_string(lines)
            elif response == "s":
                if save(filename, lines):
                    original_lines = lines
            elif response == "q":
                is_managing = done(filename, original_lines, lines)
            else:
                print("ERROR: invalid choice--enter one of 'AaQq'")
        else:
            response = input("[A]dd [Q]uit [a]: ").lower()
            if not response:
                response = "a"

            if response == "a":
                add_string(lines)
            elif response == "q":
                is_managing = (filename, original_lines, lines)
            else:
                print("ERROR: invalid choice--enter one of 'AaQq'")


def add_string(lines):
    item = input("Add item: ")
    if item and not lines.count(item):
        lines.append(item)
        lines.sort(key=str.lower)


def delete_string(lines):
    response = input("Delete item number (or 0 to cancel): ")
    try:
        num = int(response)

        if num == 0:
            return
        else:
            lines.pop(num - 1)
    except ValueError as e:
        print(f"Invalid item number: {response}")


def load(filename):
    fh = None
    try:
        fh = open(filename, "r")
        lines = set()
        for line in fh:
            line = line.strip()
            if line:
                lines.add(line)
        return sorted(lines)
    except EnvironmentError as e:
        print(f"File error: {e}\n")
    finally:
        fh.close()


def save(filename, lines):
    lines = sorted(set(lines))

    fh = None
    try:
        fh = open(filename, "w")
        for line in lines:
            fh.write(line)
            fh.write("\n")
        s = "" if len(lines) == 1 else "s"
        print("Saved {0} item{1} to \"{2}\"".format(len(lines), s, filename))
        return True
    except EnvironmentError as e:
        print(f"File Error: {e}")
        return False
    finally:
        fh.close()


def done(filename, original_lines, lines):
    if original_lines != lines:
        response = input("Save unsaved changes (y/n) [y]: ").lower()
        if not response:
            response = "y"

        if response == "y":
            save(filename, lines)
        elif response == "n":
            return False
        else:
            print(f"ERROR: Invalid option--enter one of 'YyNn'")
            return True
    else:
        return False


main()
