list = [899,473,84,838,3802]

smallest = list[0]
for num in list:
    if num < smallest:
        smallest = num

print("The smallest number in the list is:", smallest)