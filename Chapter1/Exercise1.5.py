number_list = []


def sort_list(list_in):
    new_list = []
    while list_in:
        lowest = None
        for j in range(0, len(list_in)):
            if lowest is None or list_in[j] < lowest:
                lowest = list_in[j]
            j += 1
        list_in.remove(lowest)
        new_list.append(lowest)
    while new_list:
        list_in.append(new_list[0])
        new_list.remove(new_list[0])
    return list_in


def median(list_in):
    if len(list_in) // 2 == len(list_in) / 2:  # even list
        low_index = int(len(list_in) / 2 - 1)
        high_index = low_index + 1
        return (list_in[low_index] + list_in[high_index]) / 2
    else:
        return list_in[len(list_in) // 2]


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
print("sorted: ", sort_list(number_list))
print("count = ", len(number_list),
      "sum = ", sum(number_list),
      "lowest = ", min(number_list),
      "highest = ", max(number_list),
      "mean = ", sum(number_list) / len(number_list),
      "median = ", median((sort_list(number_list))))
