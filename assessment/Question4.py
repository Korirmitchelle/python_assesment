
"""

Question: 4

Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase
letters, numbers, and symbols. The passwords should be random, generating a
new password every time the user asks for a new password.
Include your run-time code in a main method.

Hint: use Python’s random module,

"""

import random
import string

def generatePassword(strenght):
    if strenght == '3':
        n=6
        return ''.join(random.choice(string.ascii_letters) for _ in range(n))
    elif strenght == '2':
        n=9
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(n))
    else:
        n=12
        return ''.join(random.choice(string.printable) for _ in range(n))

if __name__ == "__main__":
    strenght = input("How strong do you want the password?\n\nSelect 1 for Strongestt\nSelect 2 for Average\nSelect 3 for Weakest\n\n")
    print("Your password is: ", generatePassword(strenght))


