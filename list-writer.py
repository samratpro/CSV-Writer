import csv

# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']
	
# data rows of csv file
rows = [ ['Nikhil', 'COE', '2', '9.0'],
		['Sanchit', 'COE', '2', '9.1'],
		['Aditya', 'IT', '2', '9.3'],
		['Sagar', 'SE', '1', '9.5'],
		['Prateek', 'MCE', '3', '7.8'],
		['Sahil', 'EP', '2', '9.1']
       ]

with open('test.csv', 'w') as file:
	# using csv.writer method from CSV package
	write = csv.writer(file)
	
	write.writerow(fields)
	write.writerows(rows)


# Data Writing example
import csv
datas = [
	['Samrat', '003', 'Boikali'],
	['Fahim', '013', 'Doulatpur'],
]
write_list = []
for single_data in datas:
	data_list = [single_data[0], single_data[1], single_data[2]]
	write_list.append(data_list)
	header = ['Name','ID','Address']
	with open('test.csv', 'w') as file:
		write = csv.writer(file)
		write.writerow(header)
		write.writerows(write_list)
	
