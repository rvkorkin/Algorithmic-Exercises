
def dist1D(s1, s2):    
    p = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        d = [i + 1]
        for j, c2 in enumerate(s2):
            d.append(min(p[j + 1] + 1, d[j] + 1, p[j] + (c1 != c2)))
        p = d
    return p[-1]

def WordDist(s1, s2):
    N1, N2 = len(s1), len(s2)
    d = [[0] * (N1 + 1) for _ in range(N2 + 1)]
    d[0][0] = 0
    for i in range(N1 + 1):
        d[0][i] = i
    for j in range(N2 + 1):
        d[j][0] = j
    for i in range(1, N1 + 1):
        for j in range(1, N2 + 1):
            d[j][i] = min(d[j - 1][i] + 1, d[j][i - 1] + 1, d[j - 1][i - 1] + (s1[i - 1] != s2[j - 1]))
    return d

def WordTransformer(s1, s2):
    d = WordDist(s1, s2)
    j = len(d) - 1
    i = len(d[0]) - 1
    trans = []
    while i > 0 and j >= 0:
        #equality = (s1[i - 1] == s2[j - 1])
        if d[j][i] == d[j - 1][i] + 1:
            trans.append(['insert', s2[j - 1]])
            j -= 1
        elif d[j][i] == d[j][i - 1] + 1 and (d[j][i] != d[j - 1][i] + 1):
            trans.append(['delete', s1[i - 1]])
            i -= 1
        elif (i > 0) and d[j][i] == d[j - 1][i - 1]:
            j -= 1
            i -= 1
        else:
            trans.append(['replace', s1[i - 1], s2[j - 1]])
            j -= 1
            i -= 1
    return trans[::-1]


s1 = 'abcde'
s2 = 'accdf'

if len(s2) > len(s1):
    s1, s2 = s2, s1

print(dist1D(s1, s2))
print(WordDist(s1, s2)[-1][-1])
print(WordTransformer(s1, s2))


