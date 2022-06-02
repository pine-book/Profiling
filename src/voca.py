from gettext import ngettext
import csv
CSV_FILE="./Data/oldData.csv"
Z_GEN_FILE="./Data/Zgen.txt"
old_dict = {}

def voca(n_gram_list):
    # determine the author's academic ability.
    # type_sum is length of n_gram_list
    type_sum = len(n_gram_list)
    # token_sum is variable to count duplicates
    token_sum = 0
    # count duplicates to token_sum
    for i in n_gram_list.values():
        token_sum += i
    
    # if rate of duplicates is lower than type_sum/token_sum, this author is smart.
    if 0.7 < type_sum/token_sum:
        return "This author is smart!"
    return "Oh, this author is not smart..."

def init():
    with open(CSV_FILE, "r", encoding="UTF-8", errors="", newline="") as csv1:
        # load csv file into f.
        f = csv.reader(csv1, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        for data in f:
            # add data to z_dict.
            old_dict[data[0]] = data[1]

def is_adult(n_gram_list):
    # determine the author's age based on authr's vocabulary.
    old_point = 0.0
    voca_count = 0
    
    for word, value in old_dict.items():
        if word in n_gram_list: 
            old_point += float(value)
            voca_count += 1
    if (round(old_point / voca_count,1 ) > 0.6):
        return "This author may be child"
    return "This author may be adult"

def is_Zgen(n_gram_list):
    z_gen_list = []
    with open(Z_GEN_FILE) as f:
        z_gen_list = f.read().split(",")
    if z_gen_list in n_gram_list.values():
        return "Z-gen"
    return "is not Z-gen"