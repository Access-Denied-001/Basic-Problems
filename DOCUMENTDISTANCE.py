import math
"""
	This a Document Distance which uses two strings and tells us how much similar they are!!
"""

'''	
	A good improvement here is to make a list of connectors and 
	remove them first to make our algorithm more efficient. 
	As we would have to compare only the keywords.
'''

def stringtolist(d):
    L = d.split(" ")
    mainlist = []
    for element in L:
        if element.isalnum():
            mainlist.append(element)
        else:
            sidelist = []
            for i in range(len(element)):
                if element[i].isalnum():
                    sidelist.append(element[i])
                else:
                    if len(sidelist) != 0:
                        mainlist.append("".join(sidelist))
                        sidelist.clear()
            if len(sidelist) != 0:
                mainlist.append("".join(sidelist))
                sidelist.clear()

    return mainlist


def counterforeach(list):
    countdict = dict()
    for element in list:
        if element in countdict:
            countdict[element] += 1
        else:
            countdict[element] = 1
    return countdict


def dotproduct(d1, d2):
    dotsum = 0
    presum1 = 0
    presum2 = 0
    for key in d1:
        if key in d2:
            dotsum += d1[key] * d2[key]
        presum1 += (d1[key]) ** 2
    for key in d2:
        presum2 += (d2[key]) ** 2
    mag1 = presum1 ** (0.5)
    mag2 = presum2 ** (0.5)
    return math.acos(abs(dotsum / (mag1 * mag2)))


def percentage(num):
    return 100 * (1 - (num / 1.57079632679))


d1 = "This is a random string which, I am @HFG#OAMSKFNJ to use for document distancing."
d2 = "This is the second string which, I am going to use to compare with first strin.g."
l1 = counterforeach(stringtolist(d1))
l2 = counterforeach(stringtolist(d2))
print(percentage(dotproduct(l1, l2)))
