import sys
input=sys.stdin.readline

st=input()
ans=""
for i in st:
    if i=="U" and ans=="":
        ans+=i
    elif i=="C" and ans=="U":
        ans+=i
    elif i=="P" and ans=="UC":
        ans+=i
    elif i=="C" and ans=="UCP":
        ans+=i
    elif ans=="UCPC":
        break

if ans=="UCPC":
    print("I love UCPC")
else:
    print("I hate UCPC")
    
'''
평범한 문자열 문제
'''
