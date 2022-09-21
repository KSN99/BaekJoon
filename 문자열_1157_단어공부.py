words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words :
    cnt = words.count(x)
    cnt_list.append(cnt)  # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) >=2 :  # count 숫자 최대값이 중복되면 
    #MISSISSIPI # unuque_words[M,I,S,P]    BAAA  [B,A]
    #CNT_LIST=[1,4,4,1]                     [1,3]
    print('?')
else :
    print(unique_words[(cnt_list.index(max(cnt_list)))])