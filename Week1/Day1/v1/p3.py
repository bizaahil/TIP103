def tiggerfy(word):


    word = word.lower()

    remove = ["t", "i", "gg", "er"]

    for i in remove:
        word = word.replace(i, "")

    return word

word = "Trigger"
print(tiggerfy(word))

word = "eggplant"
print(tiggerfy(word))

word = "Choir"
print(tiggerfy(word))


'''

so just remove "t", "i", "gg", "er" from any word

my plan:
make a dict with all substrings
traverse through each substring to se


'''
