import json 									#For reading the Data.json files

from difflib import get_close_matches 		   	#Importing Method to catch the related words
 
Data=json.load(open("076 data.json")) 			#Reading json file from the working Directory

def Meaning(Word): 								#Method to translate the word
 	
	Word=Word.lower()  							#Converting the inputted word in to lowercase as all the word in Data.json file is in lower case

	if Word in Data:
		print "Meaning of Word %s is :" %(Word) + "".join(Data[Word])
	elif len(get_close_matches(Word , Data.keys())) > 0 :			#Finding the related word matches to the given word
		print "Is that what you have searched for %s" %(get_close_matches(Word,Data.keys())[0])
		if raw_input('Enter Yes if you have searched for this: ').lower()  ==  'yes' :
			print "Meaning of Word %s is :" %(get_close_matches(Word,Data.keys())[0]) + "".join(Data[get_close_matches(Word,Data.keys())[0]])
	else :
		print "You searched for the wrong Word TraceBack"		


Meaning(raw_input("Enter the Word that You Want to Search: "))  #Taking Input form the user

