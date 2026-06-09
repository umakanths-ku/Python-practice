#Pyhton file detection 
 
import os 

file_path ="C:/Users/HP/Desktop/text.txt"

if os.path.exists(file_path):
    print(f"The location {file_path} exists")

    if os.path.isfile(file_path):
        print("that is a file")

    elif os.path.isdir(file_path):
        print("That is a directory") 

else:
    print("That location doesnt exists")    