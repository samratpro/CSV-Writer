import csv
#CSV Header
header = ['company_name', 'postion', 'location']

#Data
company_name = ['Tesla', 'Uniliver', 'Akij']
postion = ['Python Programming', 'Driver', 'Engineer']
location = ['USA', 'Dhaka', 'Khulna']

i = 0 #list Index and Loop
dicts_list = [] #Dict List
while i < len(company_name):
   dicts = {} #Write New Dict For Each While_Loop
   dicts['company_name'] = company_name[i]
   dicts['postion'] = postion[i]
   dicts['location'] = location[i]
   dicts_list.append(dicts) #Adding New List For Each While_Loop With Existing Data

   print(i)
   print(dicts)
   print(dicts_list)

   i += 1

print(i)
print(dicts)
print(dicts_list)

#List to CSV
with open('test.csv', 'w') as file:
  writer = csv.DictWriter(file, fieldnames = header)  #CSV Writer
  writer.writeheader() #Write CSV Header
  writer.writerows(dicts_list) #Write CSV Rows
  file.close()
