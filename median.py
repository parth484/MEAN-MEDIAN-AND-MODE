import pandas as pd

df = pd.read_csv("data.csv")
data = df["Height(Inches)"].tolist()
print(data[1])

length = len(data)
# to arrange all the values in data array in order
data.sort()
print(data[12500])

median1 = data[int((length/2))-1]
median2 = data[int(length/2)]

Median = (median1+median2)/2
print(Median)
