t = int(input())

for i in range(t):
    sentence = input()
    new_list= sentence.split()
    output = []
    for j in new_list:
        new_j=j[ : :-1]
        output.append(new_j)
    for i in output:
        print(i, end=' ')
