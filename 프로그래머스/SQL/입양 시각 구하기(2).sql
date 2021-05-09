SET @hour = -1; # 로컬변수 사용시 set을 이용할때만 = 사용
SELECT 
    (@hour := @hour+1) hour,  # 그 외엔 :=
    (select count(hour(datetime)) from animal_outs where hour(datetime)=@hour ) count
from animal_outs
where @hour<23
