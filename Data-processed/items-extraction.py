import csv

input_file = 'Data-raw/Filtered_Crops_AllData_Normalized.csv'
output_file = 'Data-raw/Unique_Items.csv'

unique_items = set()

with open(input_file, mode='r', newline='', encoding='ISO-8859-1') as infile:
    reader = csv.DictReader(infile)
    
    for row in reader:
        unique_items.add(row['Item'])

with open(output_file, mode='w', newline='', encoding='ISO-8859-1') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Item'])
    
    for item in unique_items:
        writer.writerow([item])

print(f"Unique items have been written to {output_file}")