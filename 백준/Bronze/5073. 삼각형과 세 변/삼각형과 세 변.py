import sys

while (True):
    a, b, c = map(int, sys.stdin.readline().split())
    
    if (a == b == c == 0):
        break
    
    if (max(a, b, c) < a + b + c - max(a, b, c)):
        if (a == b == c):
            print('Equilateral')
        elif (a == b) or (b == c) or (c == a):
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Invalid')