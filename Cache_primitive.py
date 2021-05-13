# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 13:57:26 2021

@author: RKorkin
"""
import weakref
      
class My_Cash:
    class Node():
        def __init__(self, value):
            self.prev, self.next, self.value = None, None, value

    def __init__(self, MaxNumber):
        self.dict = weakref.WeakValueDictionary()
        self.head = None
        self.tail = None
        self.count = 0
        self.MaxNumber = MaxNumber
        
    def _remove(self, unit):
        prev, nxt = unit.prev, unit.next
        if prev:
            prev.next = nxt
        elif self.head == unit:
            self.head = nxt
        if nxt:
            nxt.prev = prev
        elif self.tail == unit:
            self.tail = prev
        unit.prev, unit.next = None, None
        if self.count > 0:
            self.count -= 1
        
    def _add(self, unit):
        if unit is None:
            return
        unit.prev, unit.next = self.tail, None
        if self.head is None:
            self.head = unit
        if self.tail is not None:
            self.tail.next = unit
        self.tail = unit
        self.count += 1

    def __getitem__(self, key):
        try:
            unit = self.dict[key]
        except KeyError:
            return None
        self._remove(unit)
        self._add(unit)
        return unit.value

    def __setitem__(self, key, value):
        try:
            unit = self.dict[key]
            self._remove(unit)
        except KeyError:
            if self.count == self.MaxNumber:
                self._remove(self.head)
        unit = My_Cash.Node(value)
        self._add(unit)
        self.dict[key] = unit

cash = My_Cash(5)
print('add 5 elements from zero to four')

cash[0] = 'zero'
cash[1] = 'one'
cash[2] = 'two'
cash[3] = 'three'
cash[4] = 'four'

for i in range(5):
    print('i-th element is', cash[i])

print('add 6-th element: five')

cash[5] = 'five'
for i in range(1, 6):
    print('i-th element is', cash[i])

print(cash[11])