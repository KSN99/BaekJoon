# 총 N개의 바구니
# 1번부터 N번까지 번호
# 바구니에는 공이 1개씩 들어있음.
# 처음에는 바구니에 적혀있는 번호와 같은 번호가 적힌 공이 있다.
# M번 공을 바꾸려고 한다.
# 바꿀 바구니 2개를 선택하고 두 바구니에 들어있는 공을 서로 교환한다.

N, M = map(int, input().split())

basket = [n+1 for n in range(N)] # N=5 [1,2,3,4,5]

for _ in range(M):
    i, j = map(int,input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]


for k in basket:
    print(k, end=' ')