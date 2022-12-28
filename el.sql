-- 이름에 el이 들어가는 동물 찾기
SELECT animal_id, name
  from animal_ins
 where animal_type='Dog' and lower(name) like lower('%el%')
 order by name