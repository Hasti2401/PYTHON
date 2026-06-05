a = input("Enter your file name: ")

f = open(a , "x")
    
print("Your file is created succesfully!")

file_data = input("Enter your data you've to input in file.")

with open(a, "a") as f:
    f.write(file_data + "\n")