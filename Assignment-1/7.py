def square_float(number):
  """Takes a number as input and prints its square as a float."""
  try:
    num = float(number)
    square = num * num
    print(square)
  except ValueError:
    print("Invalid input. Please enter a valid number.")

square_float(2) 
square_float(3.5) 
square_float("abc") 