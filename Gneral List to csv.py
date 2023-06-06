import csv

data = ['data 1', 'data 2', 'data 3']

with open("data.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    for item in data:
        writer.writerow([item])

print("CSV file created successfully.")
