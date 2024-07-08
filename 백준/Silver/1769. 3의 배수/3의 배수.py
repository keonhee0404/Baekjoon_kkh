def is_multiple_of_3(X):
    count = 0
    
    while len(X) > 1:
        X = str(sum(int(digit) for digit in X))
        count += 1

    result = "YES" if X in {'3', '6', '9'} else "NO"
    return count, result


X = input().strip()


count, result = is_multiple_of_3(X)


print(count)
print(result)
