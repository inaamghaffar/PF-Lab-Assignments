def stringify_and_join(integer_list):
  """
  Takes a list of integers, converts each element to a string, 
  and then joins them into a single string.
  """
  string_list = [str(num) for num in integer_list]
  return "".join(string_list)

my_list = [1, 2, 3, 4, 5]
result = stringify_and_join(my_list)
print(result) 