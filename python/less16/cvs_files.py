import csv

# with open('data.csv', newline='') as csv_file:
#     file_data = csv.reader(csv_file)
#     data = []
#     for row in file_data:
#         if 'Pupkin' in row:
#             data.append(row)

# print(data)

# for row in data:
#     name, last_name, city = row
#     print(f'Name: {name}, Last name: {last_name}, City: {city}')



###
# словарь


with open('data.csv', newline='') as csv_file:
    file_data = csv.DictReader(csv_file)
    data = []
    for row in file_data:
        data.append(row)
        if row['last'] == 'Pupkin':
            print(row)



for row in data:
    print(row)