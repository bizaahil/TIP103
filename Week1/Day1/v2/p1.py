def words_with_char(words, x):
	result = []

	for i in range(len(words)):
		if x in words[i]:
			result.append(i)
	return result

words = ["batman", "superman"]
x = "a"
print(words_with_char(words, x))

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
print(words_with_char(words, x))

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
print(words_with_char(words, x))


'''
We are given an array of words and a character x
we have to return a list of indicies of words that contain the character x

make a empty list result
we traverse through every word in words 
if word.contains(x), then add that index to the result




'''
