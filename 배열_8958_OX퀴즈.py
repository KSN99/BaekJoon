n=int(input())
for i in range(n):
    b= input()
    a=list(b)
    sum=0
    c=1
    for i in a:
        if i=='O':
            sum+=c
            c+=1
        else:
            c=1
    print(sum)