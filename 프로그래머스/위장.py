def solution(clothes):
    answer = 1
    kind={}
    for i in clothes:
        if i[1] not in kind:
            kind[i[1]]=2
        else:
            kind[i[1]]+=1
    for i in kind:
        answer*=kind[i]
    return answer-1
  
  '''
  해시 - key-value 쌍으로 데이터 저장 = dict 
  dict 사용법을 더 익히기
  '''
