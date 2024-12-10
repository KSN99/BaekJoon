#서로 다른 N개의 자연수의 합: S
#자연수 N의 최댓값 ?
import random

S = int(input())  #S:200 N:19
# 1,2,3,4,5,6,,7,8,9,10
# n(n+1)//2  if 10 -> 55  56±66 까지는 N 11개가 무조건 최대

count = 0
n = 1
while n*(n+1)//2 <= S:
    count += 1
    n += 1
print(count)