name = input("Enter your name:")
gender = input("Enter your gender:")

print("Welcome to our mall, please choose on which floor you've to go.")
print("1st floor - Cloths " "2nd floor - Electronic items " "3rd floor - Makeup items ")

floor = int(input("Enter floor number (1,2,3):"))

if floor in range(4):

    if floor == 1:
        print("Welcome to cloths section")
        print("101:baby cloths ""102:female cloths ""103:male cloths")
        
        section = int(input("Enter your section: "))

        if section == 101:
            print("Welcome to baby cloth section")
        if section == 102:
            print("Welcome to female cloth section")
        if section == 103:
            print("Welcome to male cloth section")


    if floor == 2:
        print("Welcome to electronics section")
        print("201:Mobile " "202:Laptop " "203:Headphone")

        section2 = int(input("Enter your section: "))

        if section2 == 201:
            print("Welcome to Mobile section")
        if section2 == 202:
            print("Welcome to Laptop section")
        if section2 == 203:
            print("Welcome to Headphone section")
    

    if floor == 3:
        print("Welcome to MakeUp section")

print("Thank you for visiting!")