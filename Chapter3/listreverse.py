# list.reverse() reverse the items of a list in-place.
# this means that the list object reference is reused.

mylist1 = [1, 2, 3, 4]
mylist2 = mylist1  # assign the value at mylist1 to mylist2
mylist2.reverse()  # reverse the items in mylist2
print(mylist2)  # print mylist2, as expected the items are reversed
print(mylist1)  # print mylist1, since the items are reversed in-place the order is still reversed.
