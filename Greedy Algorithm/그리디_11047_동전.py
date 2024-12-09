N, K = map(int,input().split())
coins = []
for i in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)
cnt = 0
for i in coins:
    cnt+= K // i
    K = K % i

print(cnt)
