'''variable choice program'''

#the different variables

Pizza = "You have good taste in food.."
Pasta = "That is a safe option."
Burger = "Classic never change."
Other = "I wonder what yours is."

#the menu of bosses you can fight

print("Choose your favourite food:")
print("Pizza")
print("Pasta")
print("Burger")
print("Other")

#asking user for their choice of oppenent

choice = input("Enter your choice Pizza, Pasta, Burger or Other")
if choice == "Pizza":
    print(Pizza)
elif choice == "Pasta":
    print(Pasta)
elif choice == "Burger":
    print(Burger)
elif choice == "Other":
    print(Other)
else:
    print("That wasn't an option try again.")
    
