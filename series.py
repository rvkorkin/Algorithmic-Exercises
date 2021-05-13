
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
n, a = map(int, fin.readline().split())

if a == 1:
    counter = n * (n + 1) / 2
elif n == 1:
    counter = a
else:
    s = [0] * n
    s[0] = a
    for i in range(1, n):
        s[i] = s[i - 1] + (i + 1) * a**(i + 1)
    counter = s[-1]
fout.write(str(int(counter)))
fin.close()
fout.close()
