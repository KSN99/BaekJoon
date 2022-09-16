c=int(input())

for _ in range(c):
    score=list(map(int,input().split()))        
    avg=sum(score[1:])/score[0]
    u=0
    for i in score[1:]:
        if i>avg:
            u+=1
    per=u/score[0] * 100
    print(f'{per:.3f}%')