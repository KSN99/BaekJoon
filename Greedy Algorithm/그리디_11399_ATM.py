
N = int(input())
time = list(map(int,input().split()))
time.sort()
total = 0

for i in range(N):
    for k in range(i+1):
        total+= time[k]

print(total)