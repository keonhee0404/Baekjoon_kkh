import sys

n = int(sys.stdin.readline())
stack = []
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]== '1':
        stack.append(command[1])
    elif command[0] == '2':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == '3':
        print(len(stack))
    elif command[0] == '4':
        print(1 if len(stack) == 0 else 0)
    elif command[0] == '5':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
