import math

T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    def gcd(a,b):
        return math.gcd(a,b)

    def lcm(a,b):
        return math.lcm(a,b)

    print(gcd(a,b))
# T= int(input())
# for i in range(T):
#     a,b=map(int,input().split())
#     def gcd(a,b):
#         while b>0:
#             a,b = b, a%b
#         return a
#     def lcm(a,b):
#         return a*b // gcd(a,b)
#
#     print(lcm(a,b))