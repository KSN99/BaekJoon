word=input()
min_time=0
for i in word:
    if i =='A' or i=='B' or i=='C':
        min_time+=3
    elif i == 'D' or i=='E' or i=='F':
        min_time+=4
    elif i == 'G' or i=='H' or i=='I':
        min_time+=5
    elif i == 'J' or i=='K' or i=='L':
        min_time+=6
    elif i == 'M' or i=='N' or i=='O':
        min_time+=7
    elif i == 'P' or i=='Q' or i=='R' or i=='S':
        min_time+=8
    elif i == 'T' or i=='U' or i=='V':
        min_time+=9
    elif i== 'W' or i=='X' or i=='Y' or i=='Z':
        min_time+=10 
print(min_time)