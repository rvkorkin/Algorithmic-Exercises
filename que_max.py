# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 14:37:10 2021

@author: RKorkin
"""
que = []
max_arr = []
tail = 0
K = 2
N = 5
x = [1, 3, 0, 1, 0, 0, 3]
M = len(x)
presence = [0] * N
for i in range(M):
    if len(que) < K:
        if not presence[x[i]]:
            que.append([i, x[i]])
            max_arr.append(que[-1])
            presence[x[i]] = True
        else:
            presence[x[i]] = False
    elif line[0] == '-':
        tail += 1
        max_arr.pop()
    else:
        print(max_arr[-1])
        
        
        
que = []
min_arr = []
tail = 0
with open('input.txt','r') as fin, open('output.txt','w') as fout:
    N = int(fin.readline())
    for i in range(N):
        line = fin.readline().split()
        if line[0] == '+':
            que.append(float(line[1]))
            min_arr.append(que[-1])
        elif line[0] == '-':
            tail += 1
            min_arr.pop()
        else:
            print(min_arr[-1])
            fout.write(str(min_arr[-1])+'\n')
