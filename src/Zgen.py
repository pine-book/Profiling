import os
from re import A
def search_Z(n_gram_list):
    path = os.path.join('.', 'Data', 'Zgen.txt')
    with open(path, 'r', encoding='UTF-8') as f:
        Z_word = f.read().split(',')
        string = "Z世代ではありません"
        for zw in Z_word:
            if zw in n_gram_list:
                string = "Z世代です"

    return string