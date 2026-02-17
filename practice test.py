''''the practice test thingy'''

#the variables

from operator import add


num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))

#the print statements and f-strings

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are equal")

#asking for new numbers

num3 = int(input("Enter a new number"))


#the the repeating loop

get_number = True

while get_number == True:
    num4 = int(input("Enter another number"))
    if num4 > num3:
        get_number = False
    else:
        print("try again")

#making more numbers
total = 0
num = True 

while num == True:
    num5 = int(input("Enter a number"))
    if num5 <= 100 and num5 >= 50:
        total += num5
    if total >= 200:
        print ("The number is bigger than 200")
        num = False