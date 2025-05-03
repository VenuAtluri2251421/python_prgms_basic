import random
import string

# define the length of the password
password_length = 12

# define the characters to be used in the password
characters = string.ascii_letters + string.digits + string.punctuation

# generate the password
password = ''.join(random.choice(characters) for i in range(password_length))

# print the password
print(password)
