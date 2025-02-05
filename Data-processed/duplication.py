import csv

input_file = '/home/darkarc/GreenThumb/Data-raw/Unique_Items.csv'
output_file = '/home/darkarc/GreenThumb/Data-raw/Unique_Items.csv'

# Read the CSV file and remove duplicates
with open(input_file, 'r') as infile:
    reader = csv.reader(infile)
    unique_items = sorted(set(row[0] for row in reader))

# Write the unique items back to the CSV file
with open(output_file, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    for item in unique_items:
        writer.writerow([item])