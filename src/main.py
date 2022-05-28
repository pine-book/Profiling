import re
import numpy
import codecs
import create_n_gram_list
import os

n_gram_number = [1]	
representation_type = 'WORDFORM'
frequency_threshold = 0.025

input_files = []

#for i in range(10):
input_files.append(os.path.join('.\\Data\\',"n" + str(1) + '.txt'))

number_of_documents = create_n_gram_list.count_documents(input_files)
n_gram_list = create_n_gram_list.create_n_gram_list(input_files, n_gram_number, representation_type, frequency_threshold, number_of_documents)

# create dictionary of word forms and the number of documents they occur in#
#語形とそれが出現する文書数の辞書を作成する#
print(n_gram_list)


