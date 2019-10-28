
number_list = []

while True:
    try:
        response = input("enter a number or Enter to finish: ")
        if not response:
            break
        number_list += [int(response)]
    except ValueError as err:
        print("The input is not an integer.")
    except (EOFError, KeyboardInterrupt) as err:
        break

print("numbers: ", number_list)
print("count = ", len(number_list),
      "sum = ", sum(number_list),
      "lowest = ", min(number_list),
      "highest = ", max(number_list),
      "mean = ", sum(number_list) / len(number_list))
