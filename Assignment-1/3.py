# Code
def int_to_float():
    try:
        user_input = input("Enter an integer: ")
        integer_value = int(user_input)  
        float_value = float(integer_value) 
        print("The float value is:", float_value)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

int_to_float()