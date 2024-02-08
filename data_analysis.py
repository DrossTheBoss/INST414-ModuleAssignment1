import pandas as pd

#Loads the datasets
adp_data = pd.read_csv("adp_data.csv")
weekly_data = pd.read_csv("weekly_points_data.csv")

print("Original DataFrames: \n")
print(adp_data.head())
print(weekly_data.head())
print("\n")

#adds a column that has the positon with the number lable
adp_data['position_prefix'] = adp_data['POS'].str.extract(r'([A-Za-z]+)')

#Currently the source does not have data for the coumns MFL, Fantrax and FFC
#So we are going to drop those columns to clean up the data
adp_data = adp_data.drop(columns=['MFL', 'Fantrax', 'FFC'])

print("Updated ADP data:")
print(adp_data.head())
print("\n")

positions = ["QB", "RB", "WR", "TE", "K", "DST"]
weekly_dfs = {}
adp_dfs = {}

#Filters through every position, making a DataFrame for that position
for position in positions:
   
    weekly_current_position = weekly_data[weekly_data['Pos'] == position].copy()
    weekly_dfs[position] = weekly_current_position

    adp_current_position = adp_data[adp_data["position_prefix"] == position].copy()
    adp_dfs[position] = adp_current_position

for key in weekly_dfs:
    print(key + " comparision: \n")
    print(weekly_dfs[key].head())
    print(adp_dfs[key].head())
    print("\n")


