class Node:
    def __init__(self, value=None, nxt=None, prv=None):
        self.value = value
        self.nxt = nxt
        self.prv = prv


class QList():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def push_front(self, value):
        self.length += 1
        if self.first is None:
            self.first = self.last = Node(value, None, None)
        else:
            current = self.first
            self.first.prv = self.first = Node(value, None, None)
            self.first.nxt = current

    def push_back(self, value):
        self.length += 1
        if self.first is None:
            self.last = self.first = Node(value, None, None)
        else:
            current = self.last
            self.last.nxt = self.last = Node(value, None, None)
            self.last.prv = current

    def pop_front(self):
        if self.last is None:
            return
        self.length -= 1
        if self.length == 0:
            out = self.last.value
            self.last = self.first = None
            return out
        out = self.first.value
        current = self.first.nxt
        self.first = current
        current.prv = None
        return out

    def pop_back(self):
        if self.first is None:
            return
        self.length -= 1
        if self.length == 0:
            out = self.last.value
            self.last = self.first = None
            return out
        out = self.last.value
        current = self.last.prv
        self.last = current
        current.nxt = None
        return out


my_queue = QList()


with open('input.txt', 'r') as fin, open('output.txt', 'w') as fout:
    while True:
        line = fin.readline().split()
        if len(line) > 1:
            if line[0] == '0':
                my_queue.push_back(int(line[1]))
            if line[0] == '1':
                my_queue.push_front(int(line[1]))
        else:
            if line[0] == '2':
                fout.write(str(my_queue.length) + '\n')
            if line[0] == '3':
                if my_queue.length == 0:
                    fout.write('Error!\n')
                else:
                    fout.write(str(my_queue.pop_back()) + '\n')
            if line[0] == '4':
                if my_queue.length == 0:
                    fout.write('Error!\n')
                else:
                    fout.write(str(my_queue.pop_front()) + '\n')
            if line[0] == '-1':
                break
