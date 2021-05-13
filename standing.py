
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
N = int(fin.readline())
log = [''] * N
dct = {}
for i in range(N):
    log[i] = fin.readline().rstrip('\n')
    if log[i] not in dct:
        dct[log[i]] = -1
    else:
        dct[log[i]] -= 1

srt = {k: v for k, v in sorted(dct.items(), key=lambda item: item[::-1])}
for el in srt:
    fout.write(el + ' ' + str(-srt[el]) + '\n')
fin.close()
fout.close()
