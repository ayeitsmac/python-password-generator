# This is a python password generator!

import string  # module to create your own strings
import random  # module to generate random numbers

print("*" * 45)
print('Welcome to The Python Password Generator!')  # Welcome Print
print("*" * 45)
print('\n')


characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_password():
    # user's desired length of password
    length = int(input("Enter desired password length: "))
    # shuffling the character
    random.shuffle(characters)
    password = []

    # picking random characters from the list
    for i in range(length):
        password.append(random.choice(characters))

    # shuffling the password
    random.shuffle(password)
    # converting the list to a string and removing the spaces ""
    print("".join(password))


# invoking the function
generate_password()
