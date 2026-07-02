import pandas as pd
data = {"Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [25, 30, 35, 40],
}

df = pd.DataFrame(data, index=["employee1", "employee2", "employee3", "employee4"])


#print(df.loc["employee2"])  # Accessing a row by index label


#add a new column
df["job"] = ["Engineer", "Manager", "Analyst", "Director"]
#add a new row
new_row=pd.DataFrame({"Name": ["Eve"], "Age": [28], "job": ["Designer"]},
                      index=["employee5"])
df=pd.concat([df, new_row])

print(df)