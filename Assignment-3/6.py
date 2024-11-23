list = [899,473,473,84,838,84,3802,899]

occurrences = {}
for num in list:
    occurrences[num] = occurrences.get(num, 0) + 1

print(occurrences)