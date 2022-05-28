import re
import numpy
import codecs
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

#B1 TOKENIZE_LINE---------------------------------------------------------------------------------------#
#Dunn. This function takes a line from the Congressional Record data and returns a tokenized version of the speech, as a list of words#	
def tokenize_line(line,flag):
	
	#CONVERT DOCUMENT TO LIST OF WORDS#				
	temp_list = get_document_text(line, flag)

	
	temp_list = temp_list.split()           			#Convert string into list of words
	
	temp_list_2 = []

	if flag == 'WORDFORM':
		
		temp_list_2 = temp_list
	
	elif flag == 'POS':
	
		for word in temp_list:
			tag_begin = word.find('_')
			temp_word = word[tag_begin+1:]
			temp_list_2.append(temp_word)
		

	
		
	return temp_list_2
#---------------------------------------------------------------------------------------------------------#

#B2 EXTRACT_N_GRAM--------------------------------------------------------------------------------------#
#Dunn. This function takes a list of words in the text and the N for n-grams and returns#
#A list of n-grams in the document, including duplicates.#
def extract_n_gram(document_text,n_gram_number):	
	
	temp_n_gram_list = []
	
	for g in n_gram_number:
	
		n_gram_number_temp = g
	
		for i in range(len(document_text)):	#Go through each word, looking forward for n-grams#
		
			if (i + (n_gram_number_temp - 1)) <= len(document_text):				#Make sure that N words forward is within the text#
				temp = document_text[i:i + (n_gram_number_temp)]					#Define n-gram window, moving forward only#
										
				#Start to turn list of words into single n-gram string#
				n_gram_text = ''			
					
				for z in range(len(temp)):
					if z == 0:
						n_gram_text = temp[z]
					elif z > 0:
						n_gram_text += '.' + temp[z]
				#End turn list of words into single n-gram string#
					
				temp_n_gram_list += [n_gram_text]			#Add current n-gram to n-gram list for this document#
					
	return temp_n_gram_list
#------------------------------------------------------------------------------------------------------#
#Dunn. This function takes a line from the Congressional Record data and returns the speech as a string.#
def get_document_text(line,flag):

	temp_list = line.split('\t')
	document_text = temp_list[0]
	
	document_text = document_text.lower()
	
	return document_text
#-------------------------------------------------------------------------------------------------------#

#Dunn. This function takes a list of input files containing Congressional Record data and returns the number of speech which they contain#	
def count_documents(input_files):
	
	speech_count = 0					#Initiate speech count#
	
	for file in input_files:			#Loop through all files#
		fo = codecs.open(file, 'rb', 'utf-8')
		
		for line in fo:					#Loop through all lines in file#
			speech_count += 1
		
		fo.close()						#Close each file after looping through all documents#
	
	return speech_count
#------------------------------------------------------------------------------------------------------#