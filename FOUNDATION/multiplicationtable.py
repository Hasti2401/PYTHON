n = int(input("Enter table number: "))

for i in range(1,11):
    if i == 5:
        continue
    if i == 9:
        break
    print(f"{n} X {i} = {n*i}")