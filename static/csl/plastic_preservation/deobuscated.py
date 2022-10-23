#!/usr/bin/env python3

import base64
from datetime import datetime

# writes input log_value to '.log' file with timestamp
def log_to_file(log_value):
    file_name = '.log'
    with open(file_name, 'a') as log_file:
        log_file.write('# {} {} \n'.format(datetime.now(), log_value))


# encrypts string
def encrypt(input_string):

    # offset
    b = 14695981039346656037

    # prime value
    c = 1099511628211

    # for each character in input_string
    for i in input_string:

        # writes new b value to '.log' file
        log_to_file(str(b))                          # <- #REMOVE#

        # performs XOR on b and string value, MULTIPLIES with prime value and saves to new b
        b = b ^ ord(str(i)) * c

    # XOR b with this value after final character logic
    b ^= 1152921504606846975

    # convert result to hexadecimal 
    result = str.encode(hex(b)[2:])

    # return base64 encoded hexadecimal result
    return base64.b64encode(result).decode()


# main function
def main():

    # enter plaintext password
    password = input('[*]Enter your password: ')

    # encrypts password
    encrypted_password = encrypt(password)

    # prints encrypted password
    print('[*]Your encrypted password is: {}'.format(encrypted_password))
    print('[*]And has been saved to encrypted.txt')

    # writes encrypted password to 'encrypted.txt' file
    with open('encrypted.txt', 'w') as encrypted_password_file:
        encrypted_password_file.write(encrypted_password)


# runs main function when file is called
if __name__ == '__main__':
    main() 
