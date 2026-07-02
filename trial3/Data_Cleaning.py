#Data cleaning is the process of fixing/removing incorrect data

from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent / "data.csv"
df = pd.read_csv(csv_path)

#drops columns
#df= df.drop(columns=["Legendary","No"])


#handle missing data   Removed any rows with the missing value
#df=df.dropna(subset=["Type2"])
#df=df.fillna({"Type2":"none"})


#Fix inconsistent values

#df["Type1"]=df["Type1"].replace({"Grass":"GREEN","Fire":"FIRE"})

#Standardize text(make severything lowercase)

#df["Name"]=df["Name"].str.lower()

#Fix data type
#df["Legendary"]=df["Legendary"].astype(bool)

#Remove duplicate values
#df=df.drop_duplicates()

print(df.to_string())