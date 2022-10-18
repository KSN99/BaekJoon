# 점수중 최댓값 ㅡ>M 
# 모든 점수를 점수/ M*100
# ex) 최고점수 70 수학 50 수학점수는 50/70*100

N=int(input()) #시험본 과목의 개수
avg=list(map(int,input().split()))

new_avg =[]
for i in avg:
    new_avg.append(i/max(avg)*100)

average = sum(new_avg)/N
print(average)