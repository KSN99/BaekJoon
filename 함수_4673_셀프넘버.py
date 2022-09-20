numbers = set(range(1,10001))
num_d=set()
for i in range(1,10001):
    for j in str(i):
        i +=int(j)
    num_d.add(i)

self_num = sorted(numbers - num_d)
for k in self_num:
    print(k)