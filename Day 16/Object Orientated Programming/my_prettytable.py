from prettytable import PrettyTable, from_csv
import os
import sys

table = PrettyTable()

# This is manually adding the fields myself
table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],


    ]
)

print("#\#\#\#Manually created table#/#/#/#/#")
print(table)
print("\n\n\n")

print("#\#\#\#CVS created table#/#/#/#/#")
# this takes the running path for the cvs file using path join and sys.path to create the table using a CSV instead, definitely better saves manually # noqa: E501
# creating all the rows and columns

with open(os.path.join(sys.path[0], "pokemon.csv"), "r") as csv_table:
    mytable = from_csv(csv_table)

# my_table.align = "l" #changes the alignment of ALL columns
mytable.align["Name"] = 'l'  # changes just that particular column
print(mytable)
