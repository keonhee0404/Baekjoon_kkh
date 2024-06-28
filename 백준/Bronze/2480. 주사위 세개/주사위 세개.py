a, b, c = map(int, input().split())


if a >= b and a >= c:
    max_value = a
elif b >= a and b >= c:
    max_value = b
else:
    max_value = c


if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max_value * 100)
