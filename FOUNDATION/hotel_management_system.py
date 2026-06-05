print("Available rooms:\n")

avail_rooms = {101:"Single bed", 
               102:"Single bed",
               103:"Single bed",
               104:"Single bed",
               105:"Single bed",

               201:"Double bed",
               202:"Double bed",
               203:"Double bed",
               204:"Double bed",
               205:"Double bed",
               "Price of Single bed": 700,
               "Price of Double bed": 1500,
               "Half day charges": 500
               }
for room_number, room_type in avail_rooms.items():
    print(room_number ,":", room_type)

def main():
    room_number = int(input("Enter room no: "))
    room_type = input("Single Bed or Double Bed?  ")
    halfday_fullday = input("You want room for half day or full day? ")

    if room_number in avail_rooms and avail_rooms[room_number] == room_type:
        print("Congrats! You're checked in. \n")

        print("We provide facilities like this: \n")

        facilities = {"Wi-Fi" : 0,
              "Drinking Water": 20,
              "Daily Room Cleaning": 0,
              "Parking" : 0,
              "Garden Area" : 0,
              "Indoor Games": 0,
              "Extra Bed" : 200,
              "Late Check-out": 200,
              "Decoration for Birthday/Anniversary" : 200,
              "Pickup/Drop" : 200,
              "Car Rental": 200
              }
        
        for facility_name, price in facilities.items():
            print(facility_name, ":", price)
        
        selected_facilities = []
        
        def facility():
            f = int(input("How many facilities you want? "))

            for i in range(f):
                n = input("Which facility you want? ")
                selected_facilities.append(n)
            print(f"You selected {selected_facilities} facilities")

        facility()

        def billing():
            total = 0

            if room_type == "Single bed":
                total+=700
            elif room_type == "Double bed":
                total+=1500
            
            if halfday_fullday == "Half day":
                total = 500

            for item in selected_facilities:

                if item in selected_facilities:
                    total+= facilities[item]
            
            print("\n    Your Bill")

            print("Room number: ", room_number)
            print("Room type: ", room_type)
            print("Stay type: ", halfday_fullday)
             
            print("\n Facilities you use")
            for item in selected_facilities:
                print(item ,":", facilities[item])

            print("Your Bill: ", total)

        billing()

    else:
        print("Sorry! Your check-in is failed.")

main()
