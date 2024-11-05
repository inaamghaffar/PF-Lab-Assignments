def format_string(template, *args, **kwargs):
    """
    Takes a string with placeholders and uses the format method to fill in the blanks.
    """
    try:
        formatted_string = template.format(*args, **kwargs)
        return formatted_string
    except (IndexError, KeyError) as e:
        print(f"Error formatting string: {e}")
        return None

template = "My name is {name} and I am {age} years old."
formatted = format_string(template, name="Alice", age=30)
print(formatted)  

template = "The numbers are {0}, {1}, and {2}."
formatted = format_string(template, 1, 2, 3)
print(formatted)

template = "Invalid placeholder {invalid}"
formatted = format_string(template) 