import csv

# Path to your CSV file
file_path = 'path/to/your/data.csv'

# Read the CSV file
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    # Read the header (optional)
    header = next(reader)
    print(f"Header: {header}")
    # Read the data
    for row in reader:
        print(row)
