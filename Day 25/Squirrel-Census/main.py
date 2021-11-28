import pandas as pd

#Challenge  take the CSV data from squirrel_data.csv and find all the primary colours and write it out to a CSV

data = pd.read_csv("data/squirrel_data.csv")
data["Primary Fur Color"].value_counts(dropna=False,sort=True).rename_axis("Fur Colour").reset_index(name="Amount").to_csv("data/colours.csv")
#dropna = drop those without a unique value or '' | .rename_axis and rename_index from pandas will allow us to rename the columns. |


# for some reason the tutorial didn't use in place Pandas methods and instead rather exported columns and did a len on them [?!]
