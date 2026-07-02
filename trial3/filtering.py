#keeping the rows that match a condition.
from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent / "data.csv"
df = pd.read_csv(csv_path)

#tall_pokemon=df[df["Height"]>= 2]
#Heavy_pokemon=df[df["Weight"]>= 100]
#legendayry=df[df["Legendary"]==1]
#water=df[(df["Type1"]=="Water") | (df["Type2"]=="Water")]

print(Heavy_pokemon)