import pandas as pd
import statistics
 #mean
df = pd.read_csv("data.csv")
data = df["Height(Inches)"].tolist()

sum = 0
for num in data:
    sum = sum+num
print(sum)
length = len(data)
mean = sum/length
print(mean)

mean1 = statistics.mean(data)
print(mean1)