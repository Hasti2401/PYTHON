a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

print("1 = Addition\t"
"2 =  Substraction\t" 
"3 = Multiplication\t"
"4 = Division"
)
sign = input("Enter your calculation number (1,2,3,4): ")

if sign == "1":
    print("Your addition is: ",a+b)

elif sign == "2":
    print("Your substraction is: ", a-b)

elif sign == "3":
    print("Your multiplication is: ", a*b)

elif sign == "4":
    print("Your division is:", a/b)

else:
    print("Invalid")
