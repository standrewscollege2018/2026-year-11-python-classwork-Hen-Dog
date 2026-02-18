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
        print ("The number is equal to or bigger than 200")
        num = False

print ( "Now the bar code")
barcode = "1234567890123"

#making it say the different parts of the barcode and if its valid or not
if len(barcode) == 13:
    print("This is a valid barcode")
    print("The country of origin", barcode[0:2])
    print("The manufacturer code", barcode[2:7])
    print("The product code", barcode[7:12])
else:   
    print("This is not a valid barcode")

a = 1
b = 1

loop = int(input("How many times do you want to repeat the loop? "))
for i in range(0,loop):
    a = a+b
    print (a)
    b = a+b
    print (b)


