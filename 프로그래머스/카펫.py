def solution(brown, yellow):
    answer = []
    x=3
    while True:
        chk=False
        for y in range(1,x+1):
            cnt=2*(x+y-2)
            if brown==cnt:
                if x*y==brown+yellow:
                    answer.append(x)
                    answer.append(y)
                    chk=True
                    break
        if chk==True:
                break
        else:
            x+=1
    
    return answer
  '''
  규칙찾기
  '''
