def prefix(s):
    d = [0] * (len(s) + 1)
    for i in range(2, len(d)):
        d[i] = d[i - 1]
        while s[i - 1] != s[d[i]] and d[i] > 0:
            d[i] = d[d[i]]
        if s[i - 1] == s[d[i]]:
            d[i] += 1
    return d


def find_sub(s, p):
    subs = []
    d = prefix(p + '$' + s)
    for i in range(len(p) + 1, len(d)):
        if d[i] == len(p):
            subs.append(i - 2 * len(p) - 1)
    return subs


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
s = [line[:-(line[-1] == '\n') or len(line) + 1] for line in fin]
if len(s[0]) == len(s[1]):
    shift = find_sub(s[1] + s[1], s[0])
    if len(shift):
        x = shift[0]
    else:
        x = -1
else:
    x = -1
fout.write(str(x))
fin.close()
fout.close()
