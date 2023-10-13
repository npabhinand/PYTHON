import csv
with open("weather_data.csv") as data:
    weather=csv.reader(data)
    temperture=[]
    for row in weather:
        if row[1]!="temp":
            temperture.append(row[1])
    print(temperture)
    