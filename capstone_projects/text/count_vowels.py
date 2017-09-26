# Count Vowels - 
# Enter a string and the program counts the number of vowels in the text. 
# For added complexity have it report a sum of each vowel found.


list_vowels = ['a','e','i','o','u']
stringInput = input("Enter a string and I'll compute the number of vowels in it. ").lower()

def print_vowel_counts(vowel, count):
	print ("There are %s occurences of '%s' in the string \n" % (count, vowel))

# str.count(char) returns the number of times char shows up in str
print("\nYour string is: %s" % (stringInput)) 
for item in list_vowels:
	print_vowel_counts(item, stringInput.count(item))
