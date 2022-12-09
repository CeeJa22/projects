import string
import secrets


alphabet = [x for x in string.ascii_letters]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '()', '-', '_', '=', '?', '/', '>', '.', '<', ',']
password_characters = []
password_characters.extend(symbols)
password_characters.extend(alphabet)

password_list = []

for i in range(15):
    x = secrets.choice(password_characters)
    password_list.append(x)
password = ' '.join(password_list)
print(f'Your password is: {password}')