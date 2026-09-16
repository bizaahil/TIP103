def shuffle(message, indices):


    new_message = ""

    for index in indices:
        new_message += message[index] 

    return new_message


message = "evil"
indices = [3, 1, 2, 0]
print(shuffle(message, indices))

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
print(shuffle(message, indices))

message = "abc"
indices = [2, 0, 1]
print(shuffle(message, indices))

message = "hello"
indices = [4, 3, 2, 1, 0]
print(shuffle(message, indices))


'''

we are given an string message and an int array indicies

we have to take the word and jumble it based on the indicies of the word


My plan

we assemble a new string and add letters to it whenever we get a new letter from the array
return the new string



'''