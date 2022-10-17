N = input()
 
if(int(N) < 10):
    N = '0' + N
    
check_value = int(N)
cnt = 0
while True:
    add_value = int(N[0]) + int(N[1])
    cnt += 1
    
    N = N[-1] + str(add_value)[-1]
    if(check_value == int(N)):
        break
        
print(cnt)
