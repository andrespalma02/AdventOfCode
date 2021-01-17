import re

f = open("input18.txt", "r")
ops = list()
for line in f:
    ops.append(line.replace(" ", "").replace("\n", ""))

"""
    stack = list()
    exp = ""
    flag = False
    if "(" in op:
        for letra in op:
            if (len(stack) == 0) & (len(exp) != 0):
                print(exp)
                eval(exp.replace("(", "").replace(")", ""))
                exp = ""
                flag = False
            if flag:
                exp += letra
            if letra == "(":
                stack.append("(")
                flag = True
            if letra == ")":
                stack.pop(0)

    else:
        print(exp)

"""

"""
def eval(op):
    print(op)
    stack = list()
    exp = ""
    flag = False
    if "(" not in op:
        for i in range(len(op)):
            if op[i] == "*":
                mul(op[i - 1], op[i + 1:])
            if op[i] == "+":
                sum(op[i - 1], op[i + 1:])
            if op[i] == "+":
                sub(op[i - 1], op[i + 1:])
    else:

        for letra in op:
            if (len(stack) == 0) & (len(exp) != 0):
                eval(exp[:-1])
                exp = ""
                flag = False
            if flag:
                exp += letra
            if letra == "(":
                stack.append("(")
                flag = True
            if letra == ")":
                stack.pop(0)


"""

def mul(num, exp):
    if not re.match("\d", exp):
        return num * eval(exp)
    else:
        return num * exp


def sum(num, exp):
    if not re.match("\d", exp):
        return num + eval(exp)
    else:
        return str(int(num) + int(exp))


def sub(num, exp):
    if not re.match("\d", exp):
        return num - eval(exp)
    else:
        return str(int(num) - int(exp))


eval('9+3*2-5')
