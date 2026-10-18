def format_name(first_name, last_name):
    return f"{last_name.title()}, {first_name.title()}"

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

print(f'Result: {format_name(first_name, last_name)}')