import csv
CSV_FILE="./Data/oldData.csv"
z_dict = []


def init():
    # csv_file = open(csv1, "r", encoding="UTF-8", errors="", newline="")
    with open(CSV_FILE, "r", encoding="UTF-8", errors="", newline="") as csv1:
        f = csv.reader(csv1, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        # header = next(f)
        for date in f:
            z_dict.append([date[0], date[1]])


def search_Z(n_gram_list):
    z_rate = 1.0
    for z_word in z_dict:
        if z_word[0] in n_gram_list:
            z_rate *= float(z_word[1])
    if round(z_rate,1) >= 0.8: 
        return "Z世代です"
    return "Z世代ではないです"