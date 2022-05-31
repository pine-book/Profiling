import csv
import os
CSV_FILE="./Data/oldData.csv"
z_dict = {}

with open(CSV_FILE,"r", encoding="UTF-8", errors="", newline="") as csv1:

    # csv_file = open(csv1, "r", encoding="UTF-8", errors="", newline="")
    f = csv.reader(csv1, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    # header = next(f)
    for date in f:
        z_dict[date[0]] = date[1]

for i in range(10):
    f = os.path.join("Date", "{i}.txt")
    