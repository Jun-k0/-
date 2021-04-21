import re
import sys

input=sys.stdin.readline

data=input().rstrip()
p=re.compile('(100+1+|01)+')
m=p.fullmatch(data)     # match 주의
if m:
    print("SUBMARINE")
else:
    print("NOISE")
    

'''
파이썬 정규표현식 모듈 re
https://wikidocs.net/4308 참고
'''
