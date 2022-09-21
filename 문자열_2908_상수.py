A,B= map(int,input().split())
reversed1 = int(str(A)[::-1])
reversed2 = int(str(B)[::-1])
if reversed1>reversed2:
    print(reversed1)
else:
    print(reversed2)