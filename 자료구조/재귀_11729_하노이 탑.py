cnt=0
def move(n,x,y):
    global cnt
    if n > 1:
        move(n-1, x, 6-x-y)
        cnt+=1
    print(x,y)

    if n >1:
        move(n-1, 6-x-y, y)
        cnt+=1
n= int(input())
print(cnt)
move(n,1,3)