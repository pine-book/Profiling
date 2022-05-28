import re
import numpy
import codecs
import create_n_gram_list
import os

n_gram_number = [1]	#今回は連語はなし。uni-gramのみ
representation_type = 'WORDFORM'    #謎？？？？？？？？
frequency_threshold = 0.025         #謎？？？？？？？？

input_files = []    #サンプルファイル(n1 ~ n10)のディレクトリのリスト
n_gram_list = []    #辞書のリスト(n1~ n10まである)

for i in range(10):
    input_files.append(os.path.join('.\\Data\\',"n" + str(i + 1) + '.txt'))

    number_of_documents = create_n_gram_list.count_documents(input_files)
    n_gram_list.append(create_n_gram_list.create_n_gram_list(input_files, n_gram_number, representation_type, frequency_threshold, number_of_documents))

# create dictionary of word forms and the number of documents they occur in#
#語形とそれが出現する文書数の辞書を作成する#
print(n_gram_list[3])   # これはn2の辞書を表示している


