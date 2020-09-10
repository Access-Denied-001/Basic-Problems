""" 
    This is an 'One dimensional peak finder' which finds peak of given list.
    The elements are filled in increasing order till a particular number and then 
    rest are filled in decreasing order.Eg.[1,2,3,4,5,3,2,1]
    And we call a number a peak if it is greater than or equal to its neighbours.
    By this defination we can guarantee that a peak will exist.
"""
def naivepeak(L):
    n=len(L)
    peak=-10000000000231231231230124242422222222222222222222
    for i in range(n):
        if i==0:
            if L[i]>=L[i+1]:
                peak=i
                break
        elif i==n-1:
            if L[i]>=L[i-1]:
                peak=i
                break
        else:
            if L[i]>=L[i-1] and L[i]>=L[i+1]:
                peak=i
                break
    return peak
def advancepeak(L):
    n=len(L)
    if L[n//2]<L[(n//2)-1]:
        return advancepeak(L[0:n//2])
    elif L[n//2]<L[(n//2)+1]:
        return advancepeak(L[(n//2)+1:n])
    else:
        return L[n//2]
print(advancepeak([1,1.5,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1]))
print(naivepeak([1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1]))
