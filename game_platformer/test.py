# Python 3 implementation of above approach

# Function that checks whether
# the string is in alphabetical
# order or not
def isAlphabaticOrder(s):

	n = len(s)

	for i in range(1, n):

		# if element at index 'i' is less
		# than the element at index 'i-1'
		# then the string is not sorted
		if (s[i] < s[i - 1]) :
            
			print(False)
	return True

# Driver code
if __name__ == "__main__":

	s = "aabbbccb"

	# check whether the string is
	# in alphabetical order or not
	if (isAlphabaticOrder(s)):

		print("Yes")
	else:

		print(isAlphabaticOrder(s))
