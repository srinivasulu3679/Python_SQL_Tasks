
def check_password(password):

    # Check empty password
    if password == "":
        raise ValueError("Password cannot be empty.")

    # Check minimum length
    if len(password) < 8:
        raise ValueError("Password must contain at least 8 characters.")

    # Check uppercase letter
    if not any(char.isupper() for char in password):
        raise ValueError("Password must contain an uppercase letter.")

    # Check lowercase letter
    if not any(char.islower() for char in password):
        raise ValueError("Password must contain a lowercase letter.")

    # Check number
    if not any(char.isdigit() for char in password):
        raise ValueError("Password must contain a number.")

    # Check special character
    special_characters = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    if not any(char in special_characters for char in password):
        raise ValueError("Password must contain a special character.")

    return "Password is strong."


try:

    password = input("Enter Password: ")

    result = check_password(password)

    print(result)

except ValueError as error:

    print("Error:", error)

