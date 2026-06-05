import csv

with open("DSA/employees_data.csv",  "r", encoding="latin-1") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print(row)