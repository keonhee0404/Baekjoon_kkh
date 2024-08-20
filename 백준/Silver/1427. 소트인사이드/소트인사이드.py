a = list(map(int, input().strip()))
n = len(a)

for i in range(n - 1):
    max_idx = i
    for j in range(i + 1, n):
        if a[max_idx] < a[j]:
            max_idx = j
    # 스왑 (값 교환)
    a[i], a[max_idx] = a[max_idx], a[i]

# 결과를 문자열로 변환하여 출력
print(''.join(map(str, a)))
