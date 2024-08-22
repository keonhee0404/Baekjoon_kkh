N = int(input())
cnt = N

for _ in range(N):
    words = input()
    for j in range(len(words) - 1):
        if words[j] == words[j + 1]:
            continue
        elif words[j] in words[j + 1:]:  # 이후에 같은 문자가 다시 나오면
            cnt -= 1
            break
            
print(cnt)
