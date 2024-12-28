# 주어진 수 N개 중에서 소수가 몇 개인지 찾아 출력
# 수는 1000이하의 자연수
# 2,3,5,7,11,13,17,19,23,29  소수? 1또는 자기자신으로만 나눠지는 수
N = int(input())
numbers = list(map(int, input().split()))

prime_numbers = 0
for i in numbers:
    div = 1
    div_cnt = 0
    while div <= i:
        if i % div == 0:
            """div_cnt가 2가 되면 소수 개수 추가"""
            div_cnt += 1
            div += 1
        else:
            div +=1
    if div_cnt == 2 :
        prime_numbers+=1
        div = 1
        div_cnt = 0
    else:
        div = 1
        div_cnt = 0
print(prime_numbers)