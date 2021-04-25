from collections import deque

def max_pr(priority,q):
    idx=q[0]
    max=priority[q[0]]
    for i in q:
        if max<priority[i]:
            max=priority[i]
            idx=i
    return max

def solution(priorities, location):
    answer = 0
    q=deque()
    for i in range(len(priorities)):
        q.append(i)
    while True:
        max=max_pr(priorities,q)
        p_out=q.popleft()
        if max!=priorities[p_out]:
            q.append(p_out)
        else:
            priorities[p_out]=-1
            answer+=1
            if p_out==location:
                break
    return answer
  
  '''
  코드 더 간결히?
  '''
