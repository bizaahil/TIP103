def hulk_smash(n):
    answer = []

    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            answer.append("HulkSmash")
        elif i % 3 == 0:
            answer.append("Hulk")
        elif i % 5 == 0:
            answer.append("Smash")
        else:
            answer.append(str(i))

    return answer
        

n = 3
print(hulk_smash(n))

n = 5
print(hulk_smash(n))

n = 15
print(hulk_smash(n))



'''
we are given an int n 
we have to return "HulkSmash' if diviisble by 3 & 5, "Hulk" by 3, and "Smash" by 5

We have to traverse from 1 to n and append everything as a string to answer array



'''