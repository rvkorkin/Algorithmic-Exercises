def push(x):
    stack.append(x)


def pop():
    stack.pop()


stack = []


fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
with open('input.txt', 'r') as fin:
    for el in fin.readline():
        if el == '[' or el == '(' or el == '{':
            push(el)
        else:
            if el == ']':
                if len(stack) > 0 and stack[-1] == '[':
                    pop()
                else:
                    push(-9999)
                    break
            if el == ')':
                if len(stack) > 0 and stack[-1] == '(':
                    pop()
                else:
                    push(-9999)
                    break
            if el == '}':
                if len(stack) > 0 and stack[-1] == '{':
                    pop()
                else:
                    push(-9999)
                    break
if stack == []:
    fout.write('yes')
else:
    fout.write('no')

fout.close()
