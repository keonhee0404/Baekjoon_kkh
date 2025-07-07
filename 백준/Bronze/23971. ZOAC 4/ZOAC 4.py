from math import ceil

h, w, n, m = map(int, input().split())

rows = ceil(h / (n + 1))  # (n+1) 간격으로 행 선택
cols = ceil(w / (m + 1))  # (m+1) 간격으로 열 선택

print(rows * cols)
