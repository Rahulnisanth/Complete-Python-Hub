
# PALINDROME IDENTIFIER :
import re # Importing regular expression for skipping the characters other than alphabets
def is_palindrome(phrase):
    forward = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backward = forward[::-1] # Reversing original phrase
    return (forward == backward)
















