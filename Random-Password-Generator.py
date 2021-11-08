import random
# Accepts value from the user

user_input = int(input('How many password do you want: '))
user_length = int(input('Input length of you password: '))
char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# Code for random password generator

for i in range(user_input):
    password = ' '
    for j in range(user_length):
        password += random.choice(char)
    print(password)
