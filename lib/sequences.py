#!/usr/bin/env python3

def print_fibonacci(length):
    n1 = 0
    n2 = 1
    n3 = n1 + n2
    l = []
    for n in range(length):
        l.append(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
    print(l)