import pandas
data_dict={
    "student":['arjun','usman','ajsar']
    ,"marks":[75,85,90]
}

df=pandas.DataFrame(data_dict)
df.to_csv("Marks.csv")
# print(df)