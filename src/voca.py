from gettext import ngettext
import csv
CSV_FILE="./Data/oldData.csv"
Z_GEN_FILE="./Data/Zgen.txt"
old_dict = {}

#-------------------------------------------------------------
# The function is the percentage of Types and Token the sentence,
# and if the probability is less than 70%, it is not wise, and 
# if it is greater than that, it is wise.This 
#--------------------------------------------------------------
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

#This loading test data from csv file for is_adult() functions.
def init():
    with open(CSV_FILE, "r", encoding="UTF-8", errors="", newline="") as csv1:
        # load csv file into f.
        f = csv.reader(csv1, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        for data in f:
            # add data to z_dict.
            old_dict[data[0]] = data[1]
#---------------------------------------------------------
# This function determines that the more points of a word
# in a sentence 5 or less in the sentence, the more it 
# is judged to be a child.
#---------------------------------------------------------
# TestData: Data/oldDdata.py 
def is_adult(n_gram_list):
    # determine the author's age based on authr's vocabulary.
    old_point = 0
    voca_count = 0
    
    for word, value in old_dict.items():
        if word in n_gram_list: 
            if 1 > float(value):
                old_point += 1
    print(old_point)
    if (old_point < 5):
        return "This author may be child"
    return "This author may be adult"

#---------------------------------------------
# This function that test data from Z_GEN_FILE 
# includes the sentennces, returning Zgen or not.
#-----------------------------------------------
def is_Zgen(n_gram_list):
    z_gen_list = []
    with open(Z_GEN_FILE) as f:
        z_gen_list = f.read().split(",")
    if z_gen_list in n_gram_list.values():
        return "The author is Z-gen.\n"
    return "THe author is not Z-gen.\n"