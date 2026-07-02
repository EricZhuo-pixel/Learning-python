from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent / "data.csv"
df = pd.read_csv(csv_path)


#print(df.mean(numeric_only=True))
#print(df.sum(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.min(numeric_only=True))
#Print(df.count( ))

#single column
#print(df.["Height"].mean())
#print(df.["Height"].max())
#print(df.["Height"].min())
#print(df.["Height"].count())

group=df.groupby("Type1")

print(group["Height"].mean)