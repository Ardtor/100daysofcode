# Day 25
# Dealing with Comma seperated values (CSV) files
# import csv
import pandas as pd

# # this will open and split each line to a new part of the list however this is a PITA to deal with
# with open("weather_data/weather_data.csv") as f:
#     weather_data = f.read().splitlines()

# Instead Python has a proper CSV libary

# with open("weather_data/weather_data.csv") as csv_data:
#     data = csv.reader(csv_data)  # this is an object rather than a list | csv.DictReader() could also be used to create a dictionary
#     # print (data)  # shows its an object
#     # Tutorial Challenge - Create a list of the temps in the data in INT format rather than str
#     temps = []
#     # loops through the rows of the csv object, next asks to skip over the item in data
#     next(data) #next will skip the data
#     for row in data:
#         temps.append(int(row[1]))
#         #optional we could is use
#         # for row[1] != 'temp':
#         #     temps.append(int(row[1]))
#         #
#     print(temps)

# Pandas is a library / module for dealing with tabular data such as CSV / Spreadsheets / Databases

# this command will perform the open with function, and then read and format it
panda_data = pd.read_csv("weather_data/weather_data.csv")
# print (panda_data)
# print(panda_data["temp"]) # skips all the hard work just specifying the column name panda will format it for us

# In pandas a dataframe is the entire datatable object, the series is basically a single column

# data_dict = panda_data.to_dict()
# # converts the dataframe to a dictionary of dictionaries, each column being a it's own dict
# print(data_dict["day"][0], data_dict["temp"][0], data_dict["condition"][0])  # prints the dictionary for each column

# temp_list = panda_data["temp"].to_list()  # converts the series to a list
# print(temp_list)  # prints the new list

# # this is if you wanted to do it manually
# print(f"The average temperature is {sum(temp_list)/len(temp_list):.2f}")

# #However pandas has an inbuilt mean/average function
# pd_mean = panda_data["temp"].mean()
# print(f"The average temp is {pd_mean:.2f}")

# # Challange - using Pandas find the max value
# pd_max = panda_data["temp"].max()
# print(f"The max temp is {pd_max}")

# #Pandas working with columns:
# print(panda_data["condition"])  # Treats it like a dictionary
# #This is just as valid as
# print(panda_data.condition) # treats it like a object

# Get Data in rows of the dataframe in Pandas
# sets the dataframe,then [] accesses the row that fits the critera
# print(panda_data[panda_data.day == "Monday"])

# Challenge - Pull the row of data for the day that is at the max

# print(panda_data[panda_data.temp == panda_data.temp.max()])
# Seems like it's overly complicated but boils down to dataframe[find the max temp in the column "temp" and print that row]

# monday = panda_data[
#     panda_data.day == "Monday"
# ]  # sets up the variable called Monday, and assigns it to the datarow with the name of that day
# print(monday.day)
# print(monday.temp)
# print(monday.condition)  # which means we can then call up any of the data on that row

# # Challenge find the temp and convert from C to F
# print(f"{(monday.temp * 9/5)+32}")


# Creating a dataframe from scratch

data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76,56,65],
}

new_data = pd.DataFrame(data_dict)
print(new_data)

#We can also convert this to a CSV
new_data.to_csv("new_data.csv")
