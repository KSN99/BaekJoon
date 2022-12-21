N, M, K= map(int,input().split())
Numbers = list(map(int,input().split()))

Numbers.sort()
first = Numbers[N-1]
second = Numbers[N-2]

count = M//(K+1) *K
count += M % (K+1)

result = 0
result += (count) * first
result += (M-count) * second

print(result)