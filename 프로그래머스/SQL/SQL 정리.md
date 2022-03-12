헷갈렸던 프로그래머스 SQL 문제들 모음

# 이름에 el이 들어가는 동물 찾기
https://programmers.co.kr/learn/courses/30/lessons/59047

```sql
SELECT ANIMAL_ID,NAME FROM ANIMAL_INS
WHERE UPPER(NAME) LIKE "%EL%" 
AND ANIMAL_TYPE='Dog'
ORDER BY NAME
```
포함하는 쿼리 - WHEHE name LIKE %keyword% 기억하쟈.

# 입양 시각 구하기(1)
https://programmers.co.kr/learn/courses/30/lessons/59412

```sql
SELECT HOUR(DATETIME) AS HOUR,COUNT(DATETIME) FROM ANIMAL_OUTS
WHERE HOUR(DATETIME)>=9 AND HOUR(DATETIME)<20
GROUP BY HOUR(DATETIME)
ORDER BY HOUR(DATETIME)
```
HOUR() 로 시간 구함.
+) COUNT(DISTINCT(NAME)) 하면 중복 제거됨.

# NULL 처리하기
https://programmers.co.kr/learn/courses/30/lessons/59410

```sql
SELECT ANIMAL_TYPE, IFNULL(NAME,"No name") AS NAME,SEX_UPON_INTAKE 
FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```
IFNULL,,,을 쓰면 해당 조건이 NULL을 반환할때, 다른 값으로 설정해주나보다.

아래와 같이 IF와 IS NULL의 합으로도 표현 가능.
```sql
SELECT IF(IS NULL(NAME), "No name", NAME) as NAME
FROM ANIMAL_INS
```

# 중성화 여부 파악하기
https://programmers.co.kr/learn/courses/30/lessons/59409

```sql
SELECT ANIMAL_ID,NAME, 
CASE
    WHEN SEX_UPON_INTAKE LIKE '%Neutered%' OR SEX_UPON_INTAKE LIKE '%Spayed%'
    THEN "O"
    ELSE "X" END
AS 중성화
FROM ANIMAL_INS

ORDER BY ANIMAL_ID
```
CASE WHEN THEN END 문으로 원하는 값 설정 가능

# 없어진 기록 찾기
https://programmers.co.kr/learn/courses/30/lessons/59042

```sql
SELECT B.ANIMAL_ID,B.NAME FROM ANIMAL_INS A
RIGHT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID=B.ANIMAL_ID
WHERE A.ANIMAL_ID IS NULL
ORDER BY B.ANIMAL_ID
```
FROM A LEFT JOIN B ON 조건
JOIN문 익히자 !!

## INNER JOIN
문법은 같으나, INNER JOIN은 조건절에서의 조건이 일치하지 않는 컬럼은 조회되지 않는다. 

# 헤비 유저가 소유한 장소
https://programmers.co.kr/learn/courses/30/lessons/77487

```sql
select * from places 
where host_id in (
    select host_id from places group by host_id having count(host_id)>1
)
order by id
```
서브쿼리로 IN절 조건을 찾아내기!
