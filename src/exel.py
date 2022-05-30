import csv

csv_file = open(".\\Data\\oldData.csv","r")
reader = csv.reader(csv_file)

list1 = []
list2 = []

num = 0

for row in reader:
    for col in row:
        if num == 0:
            list1.append(col)
            num = 1
        else:
            list2.append(col)
            num= 0

            csv_file.close()

            print(list1)
            print(list2)   
