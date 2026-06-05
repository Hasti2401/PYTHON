ticket = "A-123"

user = input("You have ticket? ")
if user == "yes":
    if ticket == "A-123":
        print("Welcome to Super Class!")

        seat = input("Enter your seat (A1,A2,A3): ")

        if seat == "A1":
            print("Welcome to your A1 seat")
        elif seat == "A2":
            print("Welcome to your A2 seat")
        elif seat == "A3":
            print("Welcome to your A3 seat")
    
    food = input("What do you want to eat? (Healthy food, Fast food, Drinks)")
        
    if food == "Healthy food":
        print("Here is your food!")

    elif food == "Fast food":
        print("Here is your food!")

    elif food == "Drinks":
        print("Here is your drink!")

else:
    print("First bring your ticket")               