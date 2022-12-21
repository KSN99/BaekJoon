N=int(input()) #1260
change=[500, 100, 50, 10]
cnt = 0  #동전의 개수

for i in change:
    cnt+=N//i
    N=N%i

print(cnt)