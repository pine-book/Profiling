import os
from re import A
CSV_FILE="./Data/oldData.csv"
z_dict = []


def init():
 with open(CSV_FILE, "r", encoding="UTF-8", errors="", newline="") as csv1:
    # csv_file = open(csv1, "r", encoding="UTF-8", errors="", newline="")
    f = csv1.reader(csv1, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    # header = next(f)
    for date in f:
        z_dict.append([date[0], date[1]])


def search_Z(n_gram_list):
    z_rate = 1
    for z_word in z_dict:
        if z_word[0] in n_gram_list:
            z_rate *= z_word[1]
        
    

def search_Z(n_gram_list):
    path = os.path.join('.', 'Data', 'Zgen.txt')
    with open(path, 'r', encoding='UTF-8') as f:
        Z_word = f.read().split(',')
        string = "Z世代ではありません"
        for zw in Z_word:
            if zw in n_gram_list:
                string = "Z世代です"

    return string