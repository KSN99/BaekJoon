K= int(input())
# K개의 줄에 정수가 1개씩 주어진다.
# 정수가 0일 경우 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
# 정수가 0일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.
# 재민이가 최종적으로 적어 낸 수의 합을 출력

stack = []

for i in range(K):
    number = int(input())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)

sum = 0
for _ in stack:
    sum += _

print(sum)