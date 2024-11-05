def float_to_int():
    try:
        user_input = input("Enter a float: ")
        float_value = float(user_input)
        integer_value = int(float_value)
        print("The integer value is:", integer_value)
    except ValueError:
        print("Invalid input. Please enter a valid float.")

float_to_int()