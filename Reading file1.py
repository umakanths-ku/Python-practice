file_path = "C:\\Users\\HP\\Desktop\\input.txt"
try:
    with open(file_path,"r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("file not found")    

except PermissionError:
    print("You do not have permission")
