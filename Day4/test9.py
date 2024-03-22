import re

def check_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

def validate_passwords(passwords):
    valid_passwords = []
    for password in passwords:
        if check_password(password):
            valid_passwords.append(password)
    return valid_passwords

# Test the function
passwords = input("Enter comma-separated passwords: ").split(',')
valid_passwords = validate_passwords(passwords)
print("Valid passwords:", ','.join(valid_passwords))
