n = int(input("Enter number: "))


'''
for i in range(n):
    for j in range(n):
        print("*", end = "")
    print()

    ***
    ***
    ***
'''

'''
for i in range(n):
    for j in range(i):
        print("*", end="")
    print()

    *
    **
    ***
'''


'''
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()

    ****
    ***
    **
    *
'''

'''
for i in range(n):
    for j in range(i):
        print("*", end="")
    print()
for i in range(n):
    for j in range(n-i):
        print("*", end="")
    print()
'''


'''
n = 4
for i in range(n):

    for j in range (n-i-1):                
        print(" ", end="")

    for i in range(i+1):
        print("*", end="")

    print()

       *
      **
     ***
    ****
'''

'''
n = 4
for i in range (n):

    for j in range(i):
        print(" ", end="")
    
    for i in range(n-i-1):
        print("*", end="")
    
    print()
'''


'''
'''
for i in range(n+1):
     
    for j in range(i):
        print("*", end="")
    
    for j in range (2*(n-i)):
        print(" ", end="")

    for j in range(i):                
        print("*", end="")

    print()

for i in range(n+1):

    for j in range(n-i):
        print("*", end="")
    
    for j in range(2*i):
        print(" ", end="")
    
    for j in range(n-i):
        print("*", end="")
    
    print()
