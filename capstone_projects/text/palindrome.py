# Palindrome
# Checks if input string is a palidrome (same whether seen forward or backwards)
# I also added in checking each individual word if string is a sentence (2 or more words)

def check_palindrome(word):
	if(word.lower() == word[::-1].lower()):
		return str("'" + word  + "'" '\tis a palindrome')
	else:
		return str("'" + word + "'" + '\tis not a palindrome')

strInput = input('What string would you like to check? Note: we ignore capitalization ')

print(check_palindrome(strInput))			# Check the entire string itself


if (len(strInput.split()) > 1):				# Check each individual word if sentence has more than one word
	print("\n\nLet's check each word")
	for word in strInput.split():
		print('\t', check_palindrome(word), end ='\n')


