def create_n_gram_list(input_files,n_gram_number,flag,threshold,number_of_documents):

	text_n_gram_dictionary = {}
	temp_n_gram_dictionary = {}
	
	for g in n_gram_number:			#Loop through each numbe rin n-gram range#
	
		current_n_gram = []
		current_n_gram.append(g)
	
		for file in input_files:			#Loop through all files#
			fo = codecs.open(file, 'rb', 'utf-8')
		
			for line in fo:					#Loop through all lines in file#
				text = tokenize_line(line,flag)	#Tokenize the line and remove meta-data#
			
			
				temp_n_gram_list = extract_n_gram(text,current_n_gram)
				temp_n_gram_list = set(temp_n_gram_list)
			
				for n_gram in temp_n_gram_list:						#Loop through n-grams from current document and add to overall list#
			
					if n_gram in temp_n_gram_dictionary:							
						temp_n_gram_dictionary[n_gram] = temp_n_gram_dictionary[n_gram] + 1	#If word n-gram already in word list, increase frequency by 1#
					
					else:
						temp_n_gram_dictionary[n_gram] = 1			               		#If word n-gram not in word list, add with frequency of 1# 
			
			print('Done with ' + file + ' N-Gram: ' + str(g))
			fo.close()						#Close each file after looping through all documents#
		
		deletion_list = []									#Initiate list of rare words to be deleted#
			
		for entry, documents in temp_n_gram_dictionary.items():		#Loop through words and the number of documents they occur in#
			if documents <= (float(threshold) * number_of_documents):
				deletion_list.append(entry)					#Create list of words to be removed#
			
		for entry in deletion_list:
			del temp_n_gram_dictionary[entry]							#Remove words on deletion list#
				
		text_n_gram_dictionary.update(temp_n_gram_dictionary)
			
	return text_n_gram_dictionary