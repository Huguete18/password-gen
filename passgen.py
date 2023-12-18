import random
import string

#length = int(input("Enter the password size:"))
#characters = string.ascii_letters + string.digits + string.punctuation
#password = "".join(random.choice(characters) for i in range(length))
#print("The generated password is: " + password)

print("Password: ")
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
chars = lower + upper + num + symbols

temp = random.sample(chars, 25)
print("".join(temp))