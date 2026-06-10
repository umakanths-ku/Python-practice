import json

file_path = "C:\\Users\\HP\\Desktop\\input2.json"
try:
    with open(file_path,"r") as file:
        content = json.load(file)
        print(content["age"])

except FileNotFoundError:
    print("file not found")    

except PermissionError:
    print("You do not have permission")
