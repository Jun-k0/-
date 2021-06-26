def solution(s):
    arr=s.split(" ")
    maxx=arr[0]
    minn=arr[0]
    for i in arr:
        if int(maxx)<int(i):
            maxx=i
        if int(minn)>int(i):
            minn=i
    ans=[]
    ans.append(minn)
    ans.append(maxx)
    answer=" ".join(ans)
    return answer
  
'''
join은 str list에 가능 !
'''
