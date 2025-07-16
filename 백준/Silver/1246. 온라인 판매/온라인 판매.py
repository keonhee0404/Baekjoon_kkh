N, M = map(int, input().split())  
P = [int(input()) for _ in range(M)]
P.sort()
max_profit = 0
max_price = 0
for i  in range(M):
            price = P[i]
            cnt = min(M-i,N)
            profit = price * cnt 
            if profit >  max_profit:
                max_profit = profit
                max_price = price
print( max_price,max_profit)

 
