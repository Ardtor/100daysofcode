# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt", "r") as f:
    names = f.read().splitlines()  # The below works as well
    # names = names.split("\n")

with open("Input/Letters/starting_letter.txt", "r") as f:
    letter = f.read()

# with open("Output/ReadyToSend/test.txt", "w") as f:
#     f.write("test\n")

for _ in names:
    new_letter = letter.replace("[name]",_)
    with open(f"Output/ReadyToSend/{_}.txt", "w") as f:
        f.write(new_letter)
