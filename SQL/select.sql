-- 조건을 상세히 볼 것!
-- 3월에 태어난 여성 회원 목록 출력하기
SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH,"%Y-%m-%d") AS DATE_OF_BIRTH
  FROM MEMBER_PROFILE
 WHERE MONTH(DATE_OF_BIRTH)=3
   AND GENDER="W"
   AND TLNO IS NOT NULL
 ORDER BY MEMBER_ID ASC

 -- 소수점 세 번째 자리에서 반올림 = 소수점 둘째자리까지 표시됨
-- 서울에 위치한 식당 목록 출력하기
# SELECT 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소,  리뷰 평균점수는 소수점 세 번째 자리에서 반올림
#   FROM REST_INFO와 REST_REVIEW
#  WHERE 서울에 위치한 식당들의
#  ORDER BY 평균점수를 기준으로 내림차순 정렬, 즐겨찾기수를 기준으로 내림차순 정렬
 
SELECT RI.REST_ID, RI.REST_NAME, RI.FOOD_TYPE, RI.FAVORITES, RI.ADDRESS
     , ROUND(AVG(RR.REVIEW_SCORE),2) ARS
  FROM REST_INFO RI
  JOIN REST_REVIEW RR
    ON RI.REST_ID=RR.REST_ID
 WHERE RI.ADDRESS LIKE "서울%"
 GROUP BY RI.REST_NAME
 ORDER BY ARS DESC, RI.FAVORITES DESC