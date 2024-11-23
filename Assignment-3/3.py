list = [899,473,84,838,3802]

largest = list[0]
for num in list:
    if num > largest:
        largest = num

print("The largest number in the list is:", largest)