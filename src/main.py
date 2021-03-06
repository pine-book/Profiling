import create_n_gram_list
import os
import voca

n_gram_number = [1]	        # We only use uni-gram.
representation_type = 'WORDFORM'    # ???
frequency_threshold = 0     # Probably between 0 and 1, with words decreasing as they get closer to 1 ?　

input_files = []    # list of sample file
n_gram_list = []    # list of dictionary (n1 ~ n10)
voca.init()         # Initialize elderly word list

for i in range(10):
    input_files.append(os.path.join('.','Data',"n" + str(i+1) + '.txt')) # read Data file (n1 ~ n10)
    input_file = [] # initialize input_file
    input_file.append(input_files[i])   # add data to input_file
    #----------------FROM HERE, We use the code taken from this site(https://github.com/jonathandunn/political_classification/blob/master/!OLD/Feature.Extraction.v.0.13.py )
    number_of_documents = create_n_gram_list.count_documents(input_file)    # count number of data file
    n_gram_list.append(create_n_gram_list.create_n_gram_list(input_file, n_gram_number, representation_type, frequency_threshold, number_of_documents))
    #----------------Here's the quote so far------------------------------------------------------------------------------
    print("This is letter number " + str(i + 1) + ".")
    # This function indicate whether adult or not 
    print(voca.voca(n_gram_list[i])) # This function display whether the author is smart or not.
    print(voca.is_adult(n_gram_list[i])) # This function display whether the author is adult or not.
    print(voca.is_Zgen(n_gram_list[i])) # This function display whether the author is Z-generation or not.