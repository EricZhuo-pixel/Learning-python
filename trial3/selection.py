from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent / "data.csv"
#df = pd.read_csv(csv_path)


#selection by column
#print(df["Name"].to_string())
#print(df["Height"].to_string())
#print(df[["Name","Height","Weight"]])

#Selection by rows
df = pd.read_csv(csv_path, index_col='Name')
#print(df.loc["Pikachu",["Height", "Weight"]])

#print(df.iloc[0:11:2, 0:3])

pokemn=input("Enter pokemon Name:")

try:
    print(df.loc[pokemn])
except KeyError:
    print(f"{pokemnon}")
