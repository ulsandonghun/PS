def solution(s):

    size = len(s)

    answer = size

    # 첫 for 문은 문자열을 자르는 단위가 증가하는 것임.
    for step in range(1,size):
    # 각 단위별 로 압축문자를 구한 다음 현재값이랑 비교해서 가장 최소값을 answer 로 넣는 것임.
        compression = ''

        prev = s[0:step]
        count=1
        # 두번째 for 문 : 해당 단위만큼 모든 문자열의 중복유무를 첫단위 + 1 부터 탐색
        for j in range(step,size,step):

            if s[j:j+step] == prev:
                count+=1
            else:
                compression+= str(count)+prev if count>=2 else prev
                count=1
                # print(compression)

                prev=s[j:j+step]
    print(compression)
    answer=min(answer,len(compression))





    return answer



print(solution('ababcdcdababcdcd'))