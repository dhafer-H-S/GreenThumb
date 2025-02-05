import csv

input_file = 'Data-raw/Crops_AllData_Normalized.csv'
output_file = 'Data-raw/Filtered_Crops_AllData_Normalized.csv'

with open(input_file, mode='r', newline='', encoding='ISO-8859-1') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    with open(output_file, mode='w', newline='', encoding='ISO-8859-1') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            if row['Area'] == 'Tunisia':
                writer.writerow(row)

print(f"Filtered rows have been written to {output_file}")