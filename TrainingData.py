import csv


def write(filename, fields, data):
    with open(filename, 'a') as Data:
        writer = csv.writer(Data)
        #writer.writerow(fields)
        writer.writerows(data)
