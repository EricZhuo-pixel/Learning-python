#series = A pandas 1 Dimensional array with axis labels. It can hold any data type (integers, strings, floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index. A Series is like a fixed-size dict in that you can get and set values by index label.
import pandas as pd


data=[100, 102, 104,300,400]
series = pd.Series(data, index=["a", "b", "c", "d", "e"])

series.loc["c"] = 200

#print(series.iloc[0]) # 100

print(series[series > 200]) # 300, 400



carbs={"day1": 1750, "day2": 1800, "day3": 2000}
series2 = pd.Series(carbs)

#series2.loc["day3"]+= 400



print(series2[series2 >= 1800])