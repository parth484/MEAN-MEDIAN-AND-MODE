import statistics
import pandas as pd

df = pd.read_csv("data.csv")
data = df["Height(Inches)"].tolist()
median = statistics.median(data)
print(median)