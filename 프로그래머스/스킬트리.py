def solution(skill, skill_trees):
    answer = 0
    al=[True]*200
    
    for i in skill_trees:
        for k in range(1,len(skill)):
            al[ord(skill[k])]=False
        idx=0
        chk=True
        for j in i:
            if idx<len(skill)-1:
                if j==skill[idx]:
                    idx+=1
                    al[ord(skill[idx])]=True
            if al[ord(j)]==False:
                chk=False
                break
        if chk==True:
            answer+=1
            
    return answer
  '''
  스킬트리가 있는 스킬만 빼서 비교하면 편할듯
  '''
