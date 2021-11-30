import random
import pandas as pd

# Day 26 - Comprehensions
# new_list =[*new_item* for *item* in *list*]

# Challenge - Create a comprehension for the below list to add 1 to it
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

# Challenge - Guess what would happen for a comprehension on a string and how you would do it
# Guess - would add each letter to the list
name = "Angela"
new_list = [letter for letter in name]
print(new_list)

# Challenge - Create a new list from a range(1,5) and double each value
r = [num * 2 for num in range(1, 5)]
print(r)

# Comprehensions with tests

# Challenge - Create a list comprehension with a test for names longer than 5 chars and if so append them
# to the new list in ALL CAPS

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# this one loops through all the names checks if they're less than 5 characters and if so add them to the list
longer_names = [name.upper() for name in names if len(name) > 5]
print(longer_names)

# Dictionary Comprehensions
# Starting with lists
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_score = {student: random.randint(1, 100) for student in names}
print(student_score)

# Starting with a dictionary
student_scores = {"Alex": 34, "Beth": 30, "Caroline": 63, "Dave": 45, "Eleanor": 95, "Freddie": 92}
# add each key:value to passed_students by comparing each key,value in student_scores but only if it's equal or above 60
passed_students = {student: score for student, score in student_scores.items() if score >= 60}
# Would give the result {'Caroline': 63, 'Eleanor': 95, 'Freddie': 92}
print(passed_students)

# Comprehensions and using Pandas and their Dataframes (df)
student_dict = {
    "students": ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"],
    "score": [55, 66, 22, 11, 44, 22],
}
student_df = pd.DataFrame(student_dict)

# Looping through the dataframe using a for loop
# Can be done but not as useful:
# for (key,value) in student_df.items():
#     print(value)

# Panda has an inbuilt looping system:

# This will loop through then print the student name and score through the row methods
for index, row in student_df.iterrows():
    print(row.students, row.score)

# this will loop through and only show Daves score.
for index, row in student_df.iterrows():
    if row.students == "Dave":
        print(row.students, row.score)
