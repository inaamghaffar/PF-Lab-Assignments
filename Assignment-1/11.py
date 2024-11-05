def print_first_and_last(input_string):
  """Takes a string as input and prints the first and last characters."""
  if input_string:
    first_char = input_string[0]
    last_char = input_string[-1]
    print(f"First character: {first_char}")
    print(f"Last character: {last_char}")
  else:
    print("Empty string provided.")