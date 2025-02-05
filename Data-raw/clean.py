import pandas as pd

# Correct path to the CSV file
file_path = 'Data-raw/cpdata.csv'
df = pd.read_csv(file_path)

# Drop the columns 'N', 'P', and 'K'
df.drop(columns=['N', 'P', 'K'], inplace=True)

# Save the modified DataFrame back to a CSV file
df.to_csv(file_path, index=False)