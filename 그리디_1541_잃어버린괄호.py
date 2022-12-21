ex=input().split("-")
nums=[]
for i in ex:
    sum = 0
    plus=i.split("+")
    for k in plus:
        sum += int(k)
    nums.append(sum)
n=nums[0]

for i in range(1,len(nums)):
    n-=nums[i]

print(n)
