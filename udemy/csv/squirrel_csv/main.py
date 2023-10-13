import pandas as pd

data=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data["Primary Fur Color"].unique())
gray_count=len(data[data["Primary Fur Color"]=="Gray"])
cinnamon_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_count=len(data[data["Primary Fur Color"]=="Black"])
data_dict={"Fur color":["Gray","Cinnamon","Black"],"Count":[gray_count,cinnamon_count,black_count]}
data=pd.DataFrame(data_dict)
data.to_csv("Squirrel_color_count.csv")
