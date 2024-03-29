class Node():
    def __init__(self, _data):
        self.data = _data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 'red'


class BRT():
    def __init__(self):
        self.nil = Node(None)
        self.nil.color = 'black'
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, _data):
        if self.search(_data):
            return
        z = Node(_data)
        z.parent = None
        z.data = _data
        z.left = self.nil
        z.right = self.nil
        z.color = 'red'
        y = None
        x = self.root
        while x != self.nil:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
        if z.parent is None:
            z.color = 'black'
            return
        if z.parent.parent is None:
            return
        self.insert_balance(z)

    def insert_balance(self, z):
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.right:
                u = z.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.left_rotate(z.parent.parent)
            else:
                u = z.parent.parent.right
                if u.color == 'red':
                    u.color = 'black'
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.right_rotate(z.parent.parent)
            if z == self.root:
                break
        self.root.color = 'black'

    def right_balance(self, z):
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                elif z == z.parent.right:
                    z = z.parent
                    self.left_rotate(z)
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                elif z == z.parent.left:
                    z = z.parent
                    self.right_rotate(z)
                z.parent.color = 'black'
                z.parent.parent.color = 'red'
                self.left_rotate(z.parent.parent)
        self.root.color = 'black'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def trans(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def search(self, value):
        return self.search_node(self.root, value)

    def search_node(self, node, value):
        if node == self.nil:
            return False
        if value == node.data:
            return True
        if value < node.data:
            return self.search_node(node.left, value)
        return self.search_node(node.right, value)

    def remove(self, value):
        if not self.search(value):
            return
        self.delete_node(self.root, value)

    def delete_node(self, node, value):
        z = self.nil
        while node != self.nil:
            if node.data == value:
                z = node
            if node.data < value:
                node = node.right
            else:
                node = node.left
        if z == self.nil:
            return
        y = z
        last_color = y.color
        if z.left == self.nil:
            x = z.right
            self.trans(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.trans(z, z.left)
        else:
            y = self.tree_min(z.right)
            last_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.trans(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.trans(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if last_color == 'black':
            self.delete_balance(x)

    def delete_balance(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.left.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def find_max(self):
        z = self.root
        while z.right != self.nil:
            z = z.right
        return z


def dist(x):
    dst = {}
    for i, el in enumerate(x):
        if el in dst:
            dst[el].append(i)
        else:
            dst[el] = [i]
    return dst


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
N, K, M = map(int, fin.readline().split())
x = list(map(int, fin.readline().split()))

if len(set(x)) <= K or K == 1:
    counter = len(set(x))
    fout.write(str(counter))
else:
    all_coord = dist(x)
    tab = BRT()
    request = [0 for _ in range(N + 1)]
    request[x[0]] = 1
    if len(all_coord[x[0]]) > request[x[0]]:
        tab.insert([all_coord[x[0]][1], x[0]])
    else:
        tab.insert([M, x[0]])
    slots = 1
    counter = 1
    i = 1
    while i < M:
        el1 = all_coord[x[i]][request[x[i]]]
        if tab.search([el1, x[i]]):
            if len(all_coord[x[i]]) > request[x[i]]:
                tab.remove([all_coord[x[i]][request[x[i]]], x[i]])
                request[x[i]] += 1
                slots -= 1
                if len(all_coord[x[i]]) > request[x[i]]:
                    tab.insert([all_coord[x[i]][request[x[i]]], x[i]])
                    slots += 1
            else:
                tab.remove([all_coord[x[i]][-1], x[i]])
                slots -= 1
        else:
            if slots < K:
                request[x[i]] += 1
                if len(all_coord[x[i]]) > request[x[i]]:
                    tab.insert([all_coord[x[i]][request[x[i]]], x[i]])
                    slots += 1
                counter += 1
            else:
                max_node = tab.find_max()
                tab.remove(max_node.data)
                slots -= 1
                request[x[i]] += 1
                if len(all_coord[x[i]]) > request[x[i]]:
                    tab.insert([all_coord[x[i]][request[x[i]]], x[i]])
                    slots += 1
                counter += 1
        i += 1
    fout.write(str(counter))
fin.close()
fout.close()
