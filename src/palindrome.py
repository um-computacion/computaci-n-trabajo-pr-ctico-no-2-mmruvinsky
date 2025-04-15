
def is_palindrome(string):

	string = ''.join(char.lower() for char in string if char.isalnum())
	if string == string[::-1]:
		return True
	else:	
		return False