list = [899,473,473,84,838,84,3802,899]

unique_numbers = []
for num in list:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("List after removing duplicates:", unique_numbers)