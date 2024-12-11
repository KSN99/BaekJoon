# 폴리오미노 2개를 무한개만큼 가지고 있음 -> AAAA, BB
# '.', 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다.
# 이때, '.'는 폴리오미노로 덮으면 안된다.
# 첫째 줄에 사전순으로 가장 앞서는 닾을 출력/ 만약 덮을 수 없다면 -1 출력


#4의 배수, 2의 배수 고려 , X가 홀수면 -1 출력 , .은 고려할 필요 없음
#4로 나누어지면 AAAA교체 (최대한 많이 나누기) 2로 나누어지면 BB교체
# . 은 인덱스 // 2 만큼 추가

board = input() # X, .


new_board=board.split(".")
A_count = 0
B_count = 0
i = 0
while i != len(new_board):
    len_X = new_board[i].count('X')
    if len_X % 2 == 0:
        A_count = len_X // 4
        len_X = len_X % 4
        B_count = len_X // 2
        len_X = len_X % 2
        new_board[i] = "AAAA" * A_count + "BB" * B_count
        i += 1
    else:
        print(-1)
        exit()

if board.count("X") % 2 == 1:
    print(-1)
else:
    str = '.'.join(new_board)
    print(str)


