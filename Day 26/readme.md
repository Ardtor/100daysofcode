# Day 26 - String/List/Dictionary comprehensions 

This is a unique feature of Python

Projects for today: 
    Using the NATO Alphabet using list/Dictionary comprehensions 

## What are comprehensions? 

Allows python to shorten creating sequences from previous sequences in one line. 

Example:

new_list =[*new_item* for *item* in *list*]

Using the above for something like 

```
numbers = [1,2,3]

new_list = []
for n in numbers:
    add_1 = n+1
new_list.append(add_1)

new_list = [2,3,4]

```

Would give : 

```
new_list = [n+1 for n in numbers]
new_list = [2,3,4]
```

## Conditional Comprehensions

new_list =[*new_item* for *item* in *list* if *test*]

This allows us to perform the comprehension ONLY if the item meets the test

```
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# this one loops through all the names checks if they're less than 5 characters and if so add them to the list
short_names = [name for name in names if len(name) < 5] 
```
The result would be : 
short_names = ['Alex', 'Beth', 'Dave']

# Dictionary Comprehensions 

Same as a list comprehension 
new_dict = {*new_key:new_value* for *item* in *list*}

Can also ben used against another dictionary 
new_dict = {*new_key:new_value* for (*key,value*) in *list*}

And can also be done against conditions
new_dict = {*new_key:new_value* for (*key,value*) in *list* if *test*}


# Pandas

## Comprehensions and using Pandas and their Dataframes (df)

Using the below setup a comrephension would look like 

new_dict = {*new_key*:*new_value* for *key,value* in *df.iterrows()*}

```
student_dict = {
    "students": ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"],
    "score": [55, 66, 22, 11, 44, 22],
}
student_df = pd.DataFrame(student_dict)

# Panda has an inbuilt looping system:

# This will loop through then print the student name and score through the row methods
for index, row in student_df.iterrows():
    print(row.students, row.score)

# this will loop through and only show Daves score.
for index, row in student_df.iterrows():
    if row.students == "Dave":
        print(row.students, row.score)


```