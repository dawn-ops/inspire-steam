# name : peter mbugua
# date : 24/02/2026
# program to perform file operations

# create new file
new_file = open("student_data .txt","r+")

# to new file
new_file.write("{student name : peter afwata , id : 213432 , email : peter@gmail.com}")



# read from the file
data = new_file.read()
print(data)
new_file.close()


# delete file
# us os module
import os
os.remove("remove.txt")



# delete folder
 