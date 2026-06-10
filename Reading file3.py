import csv

file_path = "C:\\Users\\HP\\Desktop\\test.csv"
try:
    with open(file_path,"r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[2])

except FileNotFoundError:
    print("file not found")    

except PermissionError:
    print("You do not have permission")
