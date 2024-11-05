def calculate_operations(num1, num2):
    """
    Takes two numbers as input and prints their sum, product, and quotient as integers.
    """
    try:
        num1 = int(num1)
        num2 = int(num2)

        sum_result = num1 + num2
        product_result = num1 * num2
        if num2 != 0:
            quotient_result = num1 // num2  
            print(f"Sum: {sum_result}")
            print(f"Product: {product_result}")
            print(f"Quotient (integer): {quotient_result}")
        else:
            print(f"Sum: {sum_result}")
            print(f"Product: {product_result}")
            print("Cannot divide by zero.")
    except ValueError:
        print("Invalid input. Please enter integers only.")

calculate_operations(10, 5)
calculate_operations(7, 0)
calculate_operations("abc", 2)