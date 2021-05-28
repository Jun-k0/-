def solution(n, words):
    answer = []
    dic=[]
    seq=1
    chk=True
    pre=words[0]
    for i in words:
        if len(dic)==0:
            dic.append(i)
        else:
            if i in dic or pre[-1]!=i[0]:
                chk=False
                break
            pre=i
            seq+=1
            dic.append(i)
    print(seq)
    if chk==True:
        answer.append(0)
        answer.append(0)
    else:
        answer.append(seq%n+1)
        answer.append(seq//n+1)
    return answer
    
'''
chk를 사용하지 말고 for-else문을 사용하면 편함
for-else : for 문이 끝까지 실행된다면 else문이 실행
'''
