T=int(input())

for i in range(T):
    r,s=input().split()
    for k in s:
        print(k*int(r),end='')
