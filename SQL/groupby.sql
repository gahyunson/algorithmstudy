-- REGEXP 이용해서 다수의 문자열 추출하기
-- 자동차 종류 별 특정 옵션이 포함된 자동차 수 구하기
SELECT CAR_TYPE, COUNT(CAR_ID) AS CARS 
  FROM CAR_RENTAL_COMPANY_CAR
 WHERE OPTIONS REGEXP "통풍시트|열선시트|가죽시트"
 GROUP BY CAR_TYPE
 ORDER BY CAR_TYPE


