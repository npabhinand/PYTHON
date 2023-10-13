import pandas
data=pandas.read_csv("weather_data.csv")
lists=data["temp"].to_list()
print(data["temp"].max())