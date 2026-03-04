'''rental car thingy'''

# rental car list

cars = ["Suzuki-Van", "Toyota-Corolla", "Honda-CRV", "Suzuki-Swift", "Mitsubishi-Airtrek",
"Nissan-DC-Ute", "Toyota-Previa", "Toyota-Hi-Ace", "Toyota-Hi-Ace"]

# number of seats

seats = ["2", "4", "4", "4", "4", "4", "7", "12", "12",]

# the avaliblity of the cars

avalibility = [True, True, True, True, True, True, True, True, True]

# the list on renters

renters = ["", "", "", "", "", "", "", "", ""]

# making the program a loop so the user can keep making changes if wanted

status = True
while status == True:
# shows title thingy
    print ("Welcome to our univeritys car rental")
    print("Our cars are:")
    # making the cars show in a list
    for i in range(len(cars)):
        #making it check if a car is avalible
        if avalibility[i] == True:
            status = ""
        else:
            status = "- (Unavalible)"
        print(f"{i+1} {cars[i]} ({seats[i]}) ({avalibility[i]})")