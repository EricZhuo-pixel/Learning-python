#CSV file= Comma-separated values
#JSON file= JavaScript Object Notation


from pathlib import Path
import pandas as pd

csv_path = Path(__file__).resolve().parent / "data.csv"
df = pd.read_csv(csv_path)
print(df)
#print(df.to_string())  prints all rows


#it is the same way for a json file