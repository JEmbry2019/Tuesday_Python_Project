import csv
with open('employee_birthday.txt') as cvs_file:
    csv_reader = csv.reader(cvs_file)

    with open('new_employee_birthday.csv') as new_csv_file:
        csv_writer = csv.writer(new_csv_file)


        for line in csv_reader:
            csv_writer.writerow(line)

            