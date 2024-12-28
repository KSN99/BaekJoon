#print(ord('A')) ->65
#print(ord('O')) -> 79
S = input()
answer = ''
# 65~90 90넘어가면 65부터?
# 97~122 122 넘어가면 97부터?

for x in S:
    if x.islower():
        x= ord(x)+13
        if x > 122:
            x -= 26
        answer+=chr(x)
    elif x.isupper():
        x= ord(x)+13
        if x > 90:
            x -=26
        answer+=chr(x)
    else:
        answer+=x

print(answer)