import sys

N = int(sys.stdin.readline())
stack = []
# 1. push : 정수 X를ㄹ 스택에 넣는 연산
# 2. pop : 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 3. size : 스택에 들어있는 정수의 개수를 출력한다.
# 4. empty : 스택이 비어있으면 1, 아니면 0을 출력한다.
# 5. top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# input 2, if문을 활용한 스택 기능 구현

for i in range(N):
    """리스트 출력"""
    stack_cmd = sys.stdin.readline().split()
    """push"""
    if stack_cmd[0] == "push":
        stack.append(int(stack_cmd[1]))
    """pop"""
    if stack_cmd[0] == "pop":
        if len(stack) > 0 :
            print(stack[-1])
            stack.pop()
        else: print(-1)
    """size"""
    if stack_cmd[0] == "size":
        print(len(stack))
    """empty"""
    if stack_cmd[0] == "empty":
        if len(stack) == 0 : print(1)
        else: print(0)
    """top"""
    if stack_cmd[0] == """top""":
        if len(stack) > 0 :
            print(stack[-1])
        else: print(-1)