
fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
N, M = map(int, fin.readline().split())
counter = 0
if N >= 1:
    minutes = list(map(int, fin.readline().split()))
    sorted_minutes = sorted(minutes)
    sum_mins = 0

    while counter < N:
        if sum_mins + sorted_minutes[counter] > M:
            break
        else:
            sum_mins += sorted_minutes[counter]
        counter += 1
        if sum_mins >= M:
            break

fout.write(str(int(counter)))
fin.close()
fout.close()
