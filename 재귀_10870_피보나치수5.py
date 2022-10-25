def F(n):
    if n<=1:
        return n
    return F(n-1) + F(n-2)
 

n=int(input())
print(F(n))