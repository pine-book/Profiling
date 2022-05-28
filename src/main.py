import re
import numpy
import codecs
import create_n_gram_list
import os
for i in range(10):
    filepath = os.path.join('.\\Data\\',"n" + str(i + 1) + '.txt')
    inputfiles = open(filepath, 'r')
    inputfiles.close()

# create dictionary of word forms and the number of documents they occur in#
#語形とそれが出現する文書数の辞書を作成する#
#n_gram_list = create_n_gram_list(input_files,n_gram_number,representation_type,frequency_threshold,number_of_documents)
print(filepath)