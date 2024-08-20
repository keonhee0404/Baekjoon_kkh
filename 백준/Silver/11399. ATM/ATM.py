N = int(input())
a = list(map(int, input().split()))
n = len(a)
for i in range(1, n):
    key = a[i]
    j = i - 1
    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1
    a[j + 1] = key
time=[]
current_sum=0
for i in a:
    current_sum+=i
    time.append(current_sum)

print(sum(time))