cro_alpha=['c=','c-','dz=','d-','lj','nj','s=','z=']
word=input()
cnt=0
for i in cro_alpha:
    k=word.count(i)
    cnt+=k
           
print(len(word)-cnt)


#for i in cro_alpha:
#   word=word.replace(i,'*')
#print(len(word))