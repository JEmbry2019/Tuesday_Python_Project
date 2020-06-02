import csv

with open('jeop_question.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            for row in csv_reader:
                print(row)   # added code to change appearence.
    #         print(f'\t{",".join(row)}.')
    #         line_count += 1
    # print(f'Processed {line_count} lines.')




    # CSV to a Dictionary and print

  
data = csv.DictReader(open("jeop_question.csv"))
print("CSV file as a dictionary-------------------------------------------------------------------------------:\n")
for row in data:
   print(row)

for row in data:
   print(row[''], row['department_name'], row['manager_id'])