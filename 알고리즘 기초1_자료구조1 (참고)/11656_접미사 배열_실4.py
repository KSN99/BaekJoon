S = input()
separation = []

for i in range(len(S)):
    separation.append(S[i:len(S)])

separation.sort()

for i in separation:
    print(i)