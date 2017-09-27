'''
# Pig Latin - 
# Pig Latin is a game of alterations played on the English language game. 
# To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed # (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.
# For vowels, we just add 'way' to the end
# For consonants, we examine their consonant clusters:
# 3 consonant clusters : spl/ split, /spr/ sprig, /spj/ spume, /str/ strip, /stj/ stew, /skl/ sclerotic, /skr/ screen, /skw/ squad, /skj/ skua,"

# 2-consonant clusters: /sm/, /sn/, /st/, /sw/, /sk/, /sl/, /sp/, /sf/ , /θw/, /dw/, /tw/, /θr/, /dr/, /tr/, /kw/, /kr/, /kl/, /pr/, /fr/, /br/, /gr/, /pl/, /fl/, /bl/, /gl/ and /ʃr/.
NOTE : some of the 2-consonant clusters are in the 3 consonant cluster b/c of spelling. For example, /sf corresponds to a 'sph' sound like in sphinx
'''


vowel_ending = 'way'
ending = 'ay'
vowels = 'aeiou'
consonant_clusters_2 = ['sm', 'sh', 'st','sw', 'sk', 'sl', 'sp', 'dw','th',\
                         'tw', 'dr','gl', 'bl','fl','gr','br','fr','pr','cl','cr','qu', 'tr']
consonant_clusters_3 = ['spl', 'spr', 'scr', 'ste', 'squ', 'sph', 'thw', 'shr', 'thr']

#############################################################
# Generator Function: get_pig_latin_word
# Parameters: word : word to translate
# Purpose: translates a word to pig latin
#          by examining the initial consonants/vowels
#############################################################

def get_pig_latin_word(word):
	if word[0] in vowels:   # vowel beginning so we take the vowel and consonant to the back 
		yield str( word + vowel_ending)
	elif  len(word) > 3 and word[0:3] in consonant_clusters_3:
		yield str(word[3:] + word[0:3] + ending)
	elif len(word) > 2 and word[0:2] in consonant_clusters_2:
		yield str(word[2:] + word[0:2] + ending)
	else:							
		yield str( word[1:] + word[0] + ending)



strInput = input("What string (words or sentences) would you like translated to Pig Latin?")
# for each word in the string, get the pig latin equivalent
for word in strInput.split():
	for x in get_pig_latin_word(word):
		print(x, end = ' ')


