def solution(prices):
    answer = [0]*(len(prices))
    q=[]                                 # stack
    time=0
    for idx,price in enumerate(prices):  # for 보단 느림
        time+=1
        if len(q)==0:
            q.append((price,time,idx))
        else:
            while len(q)>0:
                p=q.pop()
                if p[0]>price:
                     answer[p[2]]=time-p[1]
                else:
                     q.append(p)
                     break
            q.append((price,time,idx))       
    while len(q)>0:
        p=q.pop()
        answer[p[2]]=time-p[1]
    return answer
  
  '''
  쌓는거 - 큐/스택 생각
  '''
