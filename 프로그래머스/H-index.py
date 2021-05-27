def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(citations[0],-1,-1): # 예외처리 주의
        cnt=0
        for j in range(len(citations)):
            if citations[j]>i:
                cnt+=1
            else:
                break
        if i<=cnt and len(citations)-cnt<=i:
            answer=i
            break

    return answer
