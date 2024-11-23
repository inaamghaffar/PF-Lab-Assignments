numbers = [899,473,84,838,3802]

numbers = list(set(numbers))
numbers.sort(reverse=True)
second_largest = numbers[1]

print("The second largest number in the list is:", second_largest)