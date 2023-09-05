# IMPORTING REGEX FOR CHECKING :
import re

# Password Validator regex:
pass_pattern = re.compile(r"[a-zA-Z0-9!@#$%&*^&]{8,}\d")
# Email Validator regex:
email_pattern = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
# Prompt user for the password ->
email = input('Enter the Email: ')
password = input('Enter the password: ')
# Check for the match ->
mail = email_pattern.fullmatch(email)
access = pass_pattern.fullmatch(password)

# Printing the outputs:
print(f'Password Accessing in -->{bool(access)}<-- condition')
print(f'Email verification in -->{bool(mail)}<-- condition')


