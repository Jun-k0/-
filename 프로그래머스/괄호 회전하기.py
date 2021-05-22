from collections import deque

def solution(s):
    answer = 0
    q=deque()
    for i in s:
        q.append(i)
    for i in range(len(s)):
        chk=True
        tempq=[]
        for j in q:
            if tempq:
                if j=='(' or j=='[' or j=='{':
                    tempq.append(j)
                else:
                    temp=tempq.pop()
                    if (j==')' and temp!='(') or (j==']' and temp!='[') or (j=='}' and temp!='{'):
                        chk=False
                        break
            else:
                tempq.append(j)
        if chk==True and not tempq:
            answer+=1
            
        rot=q.popleft()
        q.append(rot)
        
    return answer
