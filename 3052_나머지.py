# 자연수 A ,B 

n= []

for _ in range(10):
    a= int(input())
    b= a % 42
    n.append(b)
s= set(n) #중복제거위해 집합으로 변경.
print(len(s))