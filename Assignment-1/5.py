# Code
bool_input = input("Enter a boolean value (True or False): ")

try:
    bool_value = eval(bool_input)  
    if isinstance(bool_value, bool):
        print(type(bool_value))
    else:
        print("Invalid input. Please enter 'True' or 'False'.")
except (NameError, SyntaxError):
    print("Invalid input. Please enter 'True' or 'False'.")