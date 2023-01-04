import random
import string

letters = string.ascii_letters

numbers = string.digits

symbols = ['!', '@', '#', '%', '^', '&']

passwordList = []

passLength = int(input("Input the length of the password: "))

numberOfLetter = random.randint(1,passLength - 2)
numberOfNumber = random.randint(1,passLength - numberOfLetter - 1) 
numberOfSymbol = passLength - numberOfLetter - numberOfNumber


for i in range(numberOfLetter):
    passwordList.append(random.choice(letters))
    
for i in range(numberOfNumber):
    passwordList.append(random.choice(numbers))
    
for i in range(numberOfSymbol):
    passwordList.append(random.choice(symbols))

random.shuffle(passwordList) 
password = ""

for i in passwordList:
    password += i
    
print(f"Pass: {password}")