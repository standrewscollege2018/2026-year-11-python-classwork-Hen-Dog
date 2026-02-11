'''demonstrait a condition statement'''

#set password
SAVED_PASSWORD = "Margit"

#ask for password and store in a variable 

password = input ("Enter your password")

#check if it is correct

if password == SAVED_PASSWORD:
    print("Correct password")
else:
     print("incorrect. Get out!")

#asking child age if you put a number lower than 13 it will be the if statement higher will be else statement

CHILD_AGE = 13

#if you put a number lower than 13 it will be the if statement higher will be else statement

print("Welcome to the zoo")
age = int(input ("how old are you"))

if age < CHILD_AGE:
     print("you pay child price")
else:
     print("You pay full price")

