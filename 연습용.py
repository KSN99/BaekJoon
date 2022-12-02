def linear_search(x,ky):
    for i in range(num):
        if x[i]==ky:
            return i
    return -1

if __name__=='__main__':
    num=int(input("원소 수를 입력: "))
    x=[None] * num
    for i in range(num):
        x[i]=int(input(f'x[{i}]: '))
    
    ky=int(input(f'검색할 값을 입력하세요: '))

    idx=linear_search(x,ky)

    if idx==-1:
        print(f'원소값 존재 x')
    else:
        print(f'검색값은 x[{idx}]에 있습니다')