N, k = map(int, input().split())
score = list(map(int, input().split()))
for i in range(N):
    for j in range(0, N - i - 1):
        if score[j] > score[j + 1]:
            temp = score[j]
            score[j] = score[j + 1]
            score[j + 1] = temp
cutline=score[-k]
print(cutline)
