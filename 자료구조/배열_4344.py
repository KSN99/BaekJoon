C=int(input())

for i in range(C):
    scores=list(map(int,input().split()))
    avg=sum(scores[1:])/scores[0]
    avg_student=[]
    for i in range(1,scores[0]+1):
        if scores[i]>avg:
            avg_student.append(scores[i]) # [80 100 ]
    new_avg=len(avg_student)/scores[0] * 100 
    print(f'{new_avg:.3f}%')
        
