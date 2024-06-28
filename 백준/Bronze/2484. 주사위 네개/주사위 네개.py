def calculate_prize(a, b, c, d):
    dice = [a, b, c, d]
    counts = [dice.count(i) for i in range(1, 7)]

    if 4 in counts:
        number = counts.index(4) + 1
        return 50000 + number * 5000
    elif 3 in counts:
        number = counts.index(3) + 1
        return 10000 + number * 1000
    elif counts.count(2) == 2:
        pairs = [i + 1 for i, count in enumerate(counts) if count == 2]
        return 2000 + pairs[0] * 500 + pairs[1] * 500
    elif 2 in counts:
        number = counts.index(2) + 1
        return 1000 + number * 100
    else:
        return max(dice) * 100

# 입력 받기
N = int(input())
max_prize = 0

for _ in range(N):
    a, b, c, d = map(int, input().split())
    prize = calculate_prize(a, b, c, d)
    if prize > max_prize:
        max_prize = prize

# 가장 높은 상금을 첫째 줄에 출력
print(max_prize)
