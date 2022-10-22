dial=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word=input()
cnt=0
for i in dial:
    for k in word:
        if k in i:
            c=dial.index(i)+3
            cnt+=c
print(cnt)