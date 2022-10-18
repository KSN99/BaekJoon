T=int(input())

for _ in range(T):
    string=input()
    list=list(string)
    sum=0
    cnt=1
    for i in range(len(list)):
        if list[i]=='O':
            sum+=cnt
            cnt+=1
        else:
            cnt=1
    print(sum)