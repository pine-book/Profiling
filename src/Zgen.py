import csv
CSV_FILE="./Data/oldData.csv"
Z_GEN_FILE="./Data/Zgen.txt"
old_dict = []


def init():
    with open(CSV_FILE, "r", encoding="UTF-8", errors="", newline="") as csv1:
        # load csv file into f.
        f = csv.reader(csv1, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        for date in f:
            # add data to z_dict.
            old_dict.append([date[0], date[1]])


def is_adult(n_gram_list):
    # determine the author's age based on authr's vocabulary.
    old_rate = 0.0
    voca_count = 0
    is_adult = 0
    
    for old_word in old_dict:
        if old_word[0] in n_gram_list:
            if old_word[1] < 0.5:
                is_adult = 1
                break
            old_rate += float(old_word[1])
            voca_count += 1
    

    if round(old_rate, 1) >= 0.8:
        return "This author may be young"
    return "This author may be older"

def is_Zgen(n_gram_list):
    z_gen_list = []
    with open(Z_GEN_FILE) as f:
        z_gen_list = f.split(",")
    