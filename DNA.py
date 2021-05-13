fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
N = int(fin.readline())
if N == 0:
    result = 0
elif N <= 2:
    result = 4**N
else:
    x = [0] * (N + 1)
    x[1], x[2], x[3] = 4, 16, 63
    for i in range(4, N + 1):
        x[i] = 3 * (x[i - 1] + x[i - 2] + x[i - 3])
    result = x[-1]
fout.write(str(result))
fin.close()
fout.close()
