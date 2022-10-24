nums=[]
for i in range(28):
    n=int(input())
    nums.append(n)

for k in range(1,31):
    if k not in nums:
        print(k)
