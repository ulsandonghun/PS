def solution(s):
    answer = 0
    answer=len(s)

    # 짜르는 단위별로 최소의 갯수를 반환 주의, step은 1부터 시작됨
    for step in range(1,len(s)):
        # 각 step 마다의 축소 문자열 저장
        compression=''
        # 최초 step 범위를 비교 대상 문자로 설정
        prev=s[0:step]
        count=1
        # 각 step 의 단위만큼 증가하며 끝까지 순회
        for i in range(step,len(s),step):
            #주의 : for 문 안에 들어가는 step 은 고정임. 변수는 가변적
            now=s[i:i+step]
            if(prev==now):
                count+=1
            else:
                if count>=2:
                    compression+= str(count)+prev
                else:
                    compression+=prev
                prev=now
                count=1
            print(compression)
        if count >= 2:
            compression += str(count) + prev
        else:
            compression+=prev
        answer=min(answer,len(compression))


    return answer


print(solution("xababcdcdababcdcd"))