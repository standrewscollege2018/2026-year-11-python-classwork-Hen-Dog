'''paracitimale practice'''

#making child age
CHILD_AGE = 12


#asking for age and weight
age=int(input ("how old are you"))
weight=int(input ("how much do you weigh"))

#the calculation for dosage
if age >= 1 and age <= 100:
    if age >= CHILD_AGE:
        print("You are recommended to take two 500 miligram tablets of paracetimale")
    else: 
        weight = int(input("Enter your weight"))
    if weight >= 1 and weight <= 200:
        dosage = weight * 10
        print(f"Recommended dosage is {dosage}mg")