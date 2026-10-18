def format_name(first_name, last_name):
    if first_name == "" or last_name == "":
        raise ValueError("First name or last name was empty")
    return f"{last_name.title()}, {first_name.title()}"

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

try:
    print(f'Result: {format_name(first_name, last_name)}')
except Exception as e:
    print(f'⚠️ An Error occurred: {e}')