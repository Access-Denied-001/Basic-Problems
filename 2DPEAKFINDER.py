import numpy


def degradednaivepeak(L):
    n = len(L)
    m = len(L[0])
    peak = -1219320320420420
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                if L[i][j] >= L[i + 1][j] and L[i][j] >= L[i][j + 1]:
                    peak = L[i][j]
            elif i == 0 and j == m - 1:
                if L[i][j] >= L[i + 1][j] and L[i][j] >= L[i][j - 1]:
                    peak = L[i][j]
            elif i == n - 1 and j == 0:
                if L[i][j] >= L[i - 1][j] and L[i][j] >= L[i][j + 1]:
                    peak = L[i][j]
            elif i == n - 1 and j == m - 1:
                if L[i][j] >= L[i - 1][j] and L[i][j] >= L[i][j - 1]:
                    peak = L[i][j]
            elif i == 0:
                if L[i][j] >= L[i][j - 1] and L[i][j] >= L[i + 1][j] and L[i][j] >= L[i][j + 1]:
                    peak = L[i][j]
            elif i == n - 1:
                if L[i][j] >= L[i - 1][j] and L[i][j] >= L[i][j - 1] and L[i][j] >= L[i][j + 1]:
                    peak = L[i][j]
            elif j == 0:
                if L[i][j] >= L[i - 1][j] and L[i][j] >= L[i + 1][j] and L[i][j] >= L[i][j + 1]:
                    peak = L[i][j]
            elif j == m - 1:
                if L[i][j] >= L[i - 1][j] and L[i][j] >= L[i][j - 1] and L[i][j] >= L[i + 1][j]:
                    peak = L[i][j]
            else:
                if L[i][j] >= L[i - 1][j] and L[i][j] >= L[i][j - 1] and L[i][j] >= L[i + 1][j] and L[i][j] >= L[i][
                    j + 1]:
                    peak = L[i][j]
    return peak


def advancepeak(L):
    A = numpy.array(L)
    n = len(L)
    m = len(L[0])
    j = m // 2

    if m == 1:
        return max(L)[0]
    else:
        Z = A[::, j:j + 1:]
        maxx = max(list(Z))
        a = list(Z).index(maxx)
        if L[a][j] < L[a][j - 1]:
            d = list(A[::, 0:j:])
            return advancepeak(d)
        elif L[a][j] < L[a][j + 1]:
            e = list(A[::, j + 1:m:])
            return advancepeak(e)
        else:
            return L[a][j]


print(degradednaivepeak([[4, 5, 10, 3], [14, 13, 12, 2], [15, 9, 11, 17], [16, 17, 19, 20]]))
print(advancepeak([[4, 5, 10, 3], [14, 13, 12, 2], [15, 9, 11, 17], [16, 17, 19, 20]]))
