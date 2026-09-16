def good_pairs(pile1, pile2, k):

    result = 0
    for i in range(len(pile1)):
        for j in range(len(pile2)):
            if pile1[i] % (pile2[j] * k) == 0:
                result += 1

    return result


pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))


'''
we are given 2 arrays & k, find good pairs

good pair is pile1[i] is divisible by pile2[j] * k
so if pile[1] % (pile2[j] * k) == 0, then its a good pair
increment result whenever possible

we need a enhanced for loop, to traverse through both arrays


'''