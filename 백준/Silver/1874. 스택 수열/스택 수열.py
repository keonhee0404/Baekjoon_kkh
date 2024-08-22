#1874
N = int(input())

current = 0
stack = []
answer = []
possible = True


for _ in range(N):
    target = int(input().strip())

    while current < target:
        current += 1
        stack.append(current)
        answer.append('+')

    
    if stack and stack[-1] == target:
        stack.pop()
        answer.append('-')
    else:
        possible = False
        break


if not possible:
    print('NO')
else:
    for method in answer:
        print(method)

        
