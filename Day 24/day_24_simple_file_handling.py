# File handling

# with open will open and assign the file at the same time then close it out without having to do file.close
with open("Day 24\my_file.txt") as new_file:
    print(new_file.read())

# the mode flag W will OVERWRITE the contents, if the file doesn't exit it will overwrite it
with open("Day 24\my_file.txt", "w") as new_file:
    new_file.write("This is a new line\n")

# now it's empty
with open("Day 24\my_file.txt") as new_file:
    print(new_file.read())

# the mode flag a will append it to the file instead of 
with open("Day 24\my_file.txt", "a") as new_file:
    new_file.write("This is another new line\n")

with open("Day 24\my_file.txt") as new_file:
    print(new_file.read())

