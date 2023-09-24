# API FOR PASSWORD SAFETY DETECTION USING PYTHON :

# importing hashlib for hashing the passwords:
import hashlib
import requests

# function definition which passes the first-half of the hashed pass-codes to website named -> "https://haveibeenpwned.com/"
def request_api_data(query):
    url = 'https://api.pwnedpasswords.com/range/' + query
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(f'Error fetching: {response.status_code}, Check the API and try again.')
    return response

# function definition to find the count of the pass-codes matched...
def check_hash_match(hashes, hash_to_match):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_match:
            return count
    return 0

# function definition to convert the pass-codes to hashed-codes...
def hash_converter(password):
    hashed = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_half, tail = hashed[:5], hashed[5:]
    response_query = request_api_data(first_half)
    return check_hash_match(response_query, tail)

# function definition of the main drive...
def password_fraud_finder(args):
    for password in args:
        count = hash_converter(password)

        if count:
            print(f"{password} was found {count} times used...\nSo, Use a better password for safety purposes.\n")
        else:
            print(f"{password} is not found to be used, Carry on with it...!!\n")


# passing the list of pass-codes :
# password_fraud_finder(['123', '009123', 'password123', 'qwertyuiyhbtgv4567'])