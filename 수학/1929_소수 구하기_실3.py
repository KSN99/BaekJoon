
"""
3~16 사이에 수를 체크하여 하나씩 출력
리스트 활용.
리스트에서 하나씩 뽑아 확인
소수 찾는 함수 생성
"""
import sys
def isPrime(i):
    if(i<2):
      return False
    for k in range(2,i):
      if(i%k==0):
        return False
    return True


M, N = map(int, sys.stdin.readline().split())

for i in range(M,N+1):
    if(isPrime(i)):
      print(i)

