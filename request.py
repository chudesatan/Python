#!/usr/bin/python3
# -*- coding: utf-8 -*-

OPERATORS = {
    '+': int.__add__,
    '-': int.__sub__,
    '*': int.__mul__,
    '/': int.__truediv__,
    '%': int.__mod__,
    '^': int.__pow__,
}

s = input("Введите выражение>").split()

stack = []
ops = OPERATORS.keys()

for elem in reversed(s):

    if elem.isdigit():
        stack.append(int(elem))
    else:
        if elem not in ops: 
            continue

        try:
            a = stack.pop()
            b = stack.pop()
        except IndexError:
            print("Недостаточное кол-во операндов")
            exit()

        try:
            temp = OPERATORS[elem](a, b)
        except ZeroDivisionError:
            print("Нельзя делить на 0")
            exit()

        stack.append(temp)

print(stack[0])
