def solution(s):
    ans=[]
    st=s.split(" ")
    for i in st:
        for idx,j in enumerate(i):
            if j.isalpha():
                if idx==0:
                    ans.append(j.upper())
                else:
                    ans.append(j.lower())
            else:
                ans.append(j)
        ans.append(" ")
    ans.pop()
    answer="".join(ans)
    return answer
  
'''
isupper() isdigit() .upper() .lower()
(구분자).join(arr)
'''
