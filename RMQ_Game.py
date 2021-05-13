from math import log2, floor, ceil


class Decomposer:
    def __init__(self):
        self.N = 2 ** int(ceil(log2(len(x))))
        self.neutral_value = float('Inf')
        self.data = [None] * (self.N - 1) + list(x)
        self.data += [self.neutral_value] * (self.N - len(x))
        for i in range(self.N - 2, -1, -1):
            self.data[i] = min(self.data[2 * i + 1], self.data[2 * i + 2])

    def rmq(self, left, right):
        left = max(0, left)
        right = min(len(x), right)
        left += self.N - 1
        right += self.N - 1
        current_min = self.neutral_value
        while left < right:
            if not left & 1:
                current_min = min(current_min, self.data[left])
                left += 1
            if not right & 1:
                right -= 1
                current_min = min(current_min, self.data[right])
            if left == right - 1:
                return current_min
            left = (left - 1) // 2
            right = (right - 1) // 2

        return current_min

    def update(self, i, v):
        i += self.N - 1
        self.data[i] = v
        while i > 0:
            i = (i - 1) // 2
            self.data[i] = min(self.data[2 * i + 1], self.data[2 * i + 2])


with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
    N, M = map(int, fin.readline().split())
    if N > 0:
        x = list(map(int, fin.readline().split()))
        y = Decomposer()

        for _ in range(M):
            s, var1, var2 = fin.readline().split()
            if s == '+':
                y.update(int(var1), int(var2))
            elif s == '?':
                y_min = y.rmq(int(var1), int(var2))
                fout.write(str(y_min) + '\n')
