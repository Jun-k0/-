def solution(s):
    answer = True
    q=[]
    for i in s:
        if len(q)==0:
            if i==')':
                return False
            else:
                q.append(i)
        else:
            if i=='(':
                q.append(i)
            else:
                p=q.pop()
    if len(q)==0:
        return True
    else:
        return False
