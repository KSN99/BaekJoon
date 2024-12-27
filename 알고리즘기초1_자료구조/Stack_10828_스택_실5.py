import sys
N = int(sys.stdin.readline())
stack = []

for i in range(N):
    stack_cmd = sys.stdin.readline()
    # 1. push X : 정수 X를 스택에 넣는 연산
    if "push" in stack_cmd:
        stack.append(stack_cmd.split()[1])
    # 2. pop : 가장 마지막에 있는 수 출력 / 스택에 정수가 없을 경우 -1 출력
    if "pop" in stack_cmd:
        if len(stack) >= 1:
            print(stack.pop())
        else:
            print(-1)
    # 3. size : 스택에 들어가 있는 정수의 개수 출력
    if "size" in stack_cmd:
        print(len(stack))
    # 4. empty : 스택이 비어있으면 1 아니면 0 출력
    if "empty" in stack_cmd:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    # 5. top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if "top" in stack_cmd:
        if len(stack) >=1:
            print(stack[-1])
        else:
            print(-1)