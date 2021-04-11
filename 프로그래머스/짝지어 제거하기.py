def solution(s):
    answer = 0
    arr=[]
    for i in s:
        if len(arr)==0:
            arr.append(i)
        else:
            pre=arr.pop()
            if i==pre:
                continue
            else:
                arr.append(pre)
                arr.append(i)
        
    if len(arr)==0:
        answer=1
    else:
        answer=0
    return answer
  
'''
문자열 짝짓는 방식
'''
