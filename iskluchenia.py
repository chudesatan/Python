#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Exersize 1
stack = []
s = input("Введите выражение").split()
for x in s:
    if x == '+':
        a = stack.pop()
        b = stack.pop()
        stack.append(a + b)
    elif x == '-':
        a = stack.pop()
        b = stack.pop()
        stack.append(a - b)
    elif x == '*':
        a = stack.pop()
        b = stack.pop()
        stack.append(a * b)
    elif x == '/':
        a = stack.pop()
        b = stack.pop()
        stack.append(a / b)
    else:
        stack.append(int(x))
print(stack[0])
