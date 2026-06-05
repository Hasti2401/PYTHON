'''
'''
with open("file.txt", "a") as f:
    f.write("Hello World")

with open("file.txt") as f:
    print(f.read())


'''
with open("file.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("file.txt") as f:
  print(f.read())
'''

f = open("myfile.txt" , "x")

# import os
# os.remove("myfile.txt")