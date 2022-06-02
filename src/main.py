import re
import numpy
import codecs
import create_n_gram_list
import os
import Zgen
import voca

n_gram_number = [1]	#今回は連語はなし。uni-gramのみ
representation_type = 'WORDFORM'    #謎？？？？？？？？
frequency_threshold = 0  #謎？おそらく０～１の間で１にちかづくと語がへる　

input_files = []    #サンプルファイル(n1 ~ n10)のディレクトリのリスト
n_gram_list = []    #辞書のリスト(n1~ n10まである)
Zgen.init() #Z世代リスト初期化
for i in range(10):
    input_files.append(os.path.join('.\\Data\\',"n" + str(i+1) + '.txt'))
    input_file = []
    input_file.append(input_files[i])
    number_of_documents = create_n_gram_list.count_documents(input_file)
    n_gram_list.append(create_n_gram_list.create_n_gram_list(input_file, n_gram_number, representation_type, frequency_threshold, number_of_documents))
    
    print("This is letter number " + str(i + 1) + ".")
    Zresult = Zgen.search_Z(n_gram_list[i])
    print(Zresult)
    education_result = voca.voca(n_gram_list[i])
    
    print(education_result)
# create dictionary of word forms and the number of documents they occur in#
#語形とそれが出現する文書数の辞書を作成する#

# print(n_gram_list[3])   # これはn4の辞書を表示している 



