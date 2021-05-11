select * from places 
where host_id in (
    select host_id from places group by host_id having count(host_id)>1
)
order by id

# In의 조건에 해당되는 컬럼을 뽑음
