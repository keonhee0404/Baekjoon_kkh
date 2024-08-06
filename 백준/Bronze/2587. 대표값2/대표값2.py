numbers=[]
for _ in range(5):
    number=int(input())
    numbers.append(number)
average=(sum(numbers)/5)
print(int(average))
for i in range(5):
    for j in range(0,5-i-1):
        if numbers[j]>numbers[j+1]:
            temp=numbers[j]
            numbers[j]=numbers[j+1]
            numbers[j+1]=temp
median=numbers[2]
print(median)
        
