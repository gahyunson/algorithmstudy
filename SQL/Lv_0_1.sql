-- 모든 레코드 조회하기
SELECT *
  FROM ANIMAL_INS
 ORDER BY ANIMAL_ID

-- 이름에 el이 들어가는 동물 찾기
SELECT ANIMAL_ID, NAME
  FROM ANIMAL_INS
 WHERE animal_type='Dog' AND lower(NAME) LIKE lower('%el%')
 ORDER BY NAME

 -- 아픈 동물 찾기
SELECT ANIMAL_ID, NAME
  FROM ANIMAL_INS
 WHERE INTAKE_CONDITION='Sick'
ORDER BY ANIMAL_ID

-- 어린 동물 찾기
SELECT ANIMAL_ID, NAME
  FROM ANIMAL_INS
 WHERE INTAKE_CONDITION!='Aged'
ORDER BY ANIMAL_ID

-- 상위 n개 레코드
SELECT NAME FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1

-- 조건에 맞는 회원수 구하기
SELECT COUNT(*) 
  FROM USER_INFO
 WHERE YEAR(JOINED)="2021"
   AND AGE BETWEEN 20 AND 29

-- 가장 비싼 상품 구하기
SELECT MAX(PRICE) AS MAX_PRICE
  FROM PRODUCT

-- 최댓값 구하기
SELECT MAX(DATETIME) AS 시간
  FROM ANIMAL_INS

-- 최솟값 구하기
SELECT DATETIME
 FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1

-- 동물 수 구하기
SELECT count(ANIMAL_ID) 
  FROM ANIMAL_INS

-- 중복 제거하기
SELECT count(DISTINCT NAME)
  FROM ANIMAL_INS
WHERE NAME IS NOT NULL

-- 코드를 입력하세요
SELECT INGREDIENT_TYPE, SUM(F.TOTAL_ORDER)
  FROM FIRST_HALF AS F
INNER JOIN ICECREAM_INFO AS II 
        ON F.FLAVOR= II.FLAVOR
GROUP BY INGREDIENT_TYPE
ORDER BY TOTAL_ORDER ASC

-- 고양이와 개는 몇 마리 있을까
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE)
  FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
HAVING ANIMAL_TYPE='Cat' OR ANIMAL_TYPE='Dog'
ORDER BY ANIMAL_TYPE

-- 동명 동물 수 찾기
SELECT * 
FROM (SELECT NAME, COUNT(NAME) AS COUNT
        FROM ANIMAL_INS
       WHERE NAME IS NOT NULL
    GROUP BY NAME
    ORDER BY NAME)  A
WHERE COUNT > 1 

-- 년, 월, 성별 별 상품 구매 회원 수 구하기
SELECT YEAR(O.SALES_DATE) AS YEAR
     , MONTH(O.SALES_DATE) AS MONTH
     , U.GENDER AS GENDER
     , COUNT(DISTINCT O.USER_ID) AS USERS
  FROM USER_INFO U, ONLINE_SALE O
 WHERE U.USER_ID = O.USER_ID
   AND GENDER IS NOT NULL
 GROUP BY YEAR, MONTH, GENDER
 ORDER BY YEAR, MONTH, GENDER

-- 한 번 더 품
# SELECT 년, 월, 성별 별로 상품을 구매한 회원수를 집계
#   FROM USER_INFO 테이블과 ONLINE_SALE 테이블에서
#  GROUP BY 년, 월, 성별 별로
# HAVING 성별 정보가 없는 경우 결과에서 제외해주세요.
#  ORDER BY  년, 월, 성별을 기준으로 오름차순 정렬

SELECT YEAR(SALES_DATE) AS YEAR
     , MONTH(SALES_DATE) AS MONTH
     , GENDER
     , COUNT(DISTINCT OS.USER_ID) AS USERS
  FROM ONLINE_SALE AS OS
  JOIN USER_INFO AS UI
    ON OS.USER_ID=UI.USER_ID
 WHERE UI.GENDER IS NOT NULL
 GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE), GENDER
 ORDER BY YEAR(SALES_DATE), MONTH(SALES_DATE), GENDER

-- 입양 시각 구하기(2)
/* WITH : 메모리상에 가상 테이블 저장
   RECURSIVE : 재귀 여부
   tb1 : 가상 테이블명 
SELECT 0시부터 23시까지 입양이 몇 건이나 발생했는지 조회
GROUP BY 각 시간대별로
ORDER BY 시간대 순으로 정렬 */
-- 가상 테이블 생성 WITH RECURSIVE
    -- index table create
WITH RECURSIVE tb1 AS (
    -- 초깃값 0 설정
    SELECT 0 AS HOUR
    UNION ALL
    -- 초깃값 이용해서 반복문 생성
    SELECT HOUR+1 FROM tb1 WHERE HOUR < 23
    -- index에 맞는 count값 설정
) , tb2 AS (
    SELECT HOUR(DATETIME) AS HOUR 
         , COUNT(DISTINCT ANIMAL_ID) AS CNT
      FROM ANIMAL_OUTS
     GROUP BY HOUR
)

-- 최종 조회문
-- 시간, 카운트수
SELECT tb1.HOUR
     , IF(tb2.CNT IS NULL, 0, CNT) AS COUNT
     # , CASE WHEN tb2.CNT IS NULL THEN 0 ELSE CNT END AS COUNT
-- 가상의 두 테이블을 합친다
FROM tb1
     LEFT JOIN tb2 
            ON tb1.HOUR = tb2.HOUR
ORDER BY HOUR


-- 이름이 있는 동물의 아이디
SELECT ANIMAL_ID 
  FROM ANIMAL_INS
WHERE NAME IS NOT NULL
ORDER BY ANIMAL_ID

-- NULL 처리하기
SELECT ANIMAL_TYPE, IFNULL(NAME, 'No name'), SEX_UPON_INTAKE
FROM ANIMAL_INS
ORDER BY ANIMAL_ID

-- 평균 일일 대여 요금 구하기
-- ROUND() 소수점 반올림
-- AVG() 평균값
SELECT ROUND(AVG(DAILY_FEE), 0) AS AVERAGE_FEE
  FROM CAR_RENTAL_COMPANY_CAR
 WHERE CAR_TYPE='SUV'

 -- 재구매가 일어난 상품과 회원 리스트 구하기
SELECT USER_ID, PRODUCT_ID -- 재구매한 회원 ID와 재구매한 상품 ID를 출력
  FROM ONLINE_SALE -- ONLINE_SALE 테이블에서 
GROUP BY USER_ID, PRODUCT_ID -- 동일한 회원이 동일한 상품을
HAVING COUNT(SALES_AMOUNT)>1 -- 재구매한 데이터를 구하여
ORDER BY USER_ID, PRODUCT_ID DESC 
-- 결과는 회원 ID를 기준으로 오름차순 정렬해주시고 회원 ID가 같다면 상품 ID를 기준으로 내림차순 정렬해주세요.
-- 문제 : ONLINE_SALE 테이블에서 동일한 회원이 동일한 상품을 재구매한 데이터를 구하여, 재구매한 회원 ID와 재구매한 상품 ID를 출력하는 SQL문을 작성해주세요. 결과는 회원 ID를 기준으로 오름차순 정렬해주시고 회원 ID가 같다면 상품 ID를 기준으로 내림차순 정렬해주세요.

-- 오프라인/온라인 판매 데이터 통합하기 
SELECT DATE_FORMAT(T1.sales_date, '%Y-%m-%d') AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT 
  FROM (SELECT * 
          FROM ONLINE_SALE
         UNION ALL
        SELECT OFFLINE_SALE_ID, NULL AS USER_ID, PRODUCT_ID, SALES_AMOUNT, SALES_DATE 
          FROM OFFLINE_SALE) T1
WHERE DATE_FORMAT(T1.sales_date, '%Y-%m') = '2022-03'
ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC

-- 즐겨찾기가 가장 많은 식당 정보 출력하기
-- 음식 종류, ID, 식당 이름, 즐겨찾기수를 조회
SELECT RI.FOOD_TYPE, RI.REST_ID, RI.REST_NAME, RI.FAVORITES
-- REST_INFO 테이블에서 음식종류별로 즐겨찾기수가 가장 많은 식당의 
  FROM (SELECT FOOD_TYPE, MAX(FAVORITES) AS MAXF -- 필터 테이블(음식종류, 가장 많은 즐겨찾기 값) 
          FROM REST_INFO -- (REST_INFO 테이블에서)
         GROUP BY FOOD_TYPE) AS MAXT -- (음식종류별로)
  JOIN REST_INFO AS RI -- REST_INFO 테이블에서 
    ON RI.FOOD_TYPE=MAXT.FOOD_TYPE -- 원테이블 + 필터 테이블 합칠 키값
 WHERE RI.FAVORITES=MAXT.MAXF -- 많은 FAVORITES 중 하나만 출력하게 함
ORDER BY FOOD_TYPE DESC -- 결과는 음식 종류를 기준으로 내림차순 정렬해주세요.

-- 경기도에 위치한 식품창고 목록 출력하기
-- SUBSTRING_INDEX
SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS
     , IF(FREEZER_YN IS NULL, "N", FREEZER_YN)
  FROM FOOD_WAREHOUSE
 WHERE SUBSTRING_INDEX(ADDRESS, " ", 1)='경기도'
 ORDER BY WAREHOUSE_ID

 -- 과일로 만든 아이스크림 고르기
 -- DESC 주의
SELECT FH.FLAVOR -- 아이스크림의 맛을
  FROM FIRST_HALF FH, ICECREAM_INFO II
 WHERE FH.FLAVOR=II.FLAVOR
   AND FH.TOTAL_ORDER > 3000 -- 아이스크림 총주문량이 3,000보다 높으면서
   AND II.INGREDIENT_TYPE='fruit_based' -- 아이스크림의 주 성분이 과일인
 ORDER BY TOTAL_ORDER DESC -- 총주문량이 큰 순서대로

 -- 역순 정렬하기
SELECT NAME, DATETIME
  FROM ANIMAL_INS
 ORDER BY ANIMAL_ID DESC

 -- 인기있는 아이스크림
SELECT FLAVOR
  FROM FIRST_HALF
 ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID

 -- 흉부외과 또는 일반외과 의사 목록 출력하기
SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, "%Y-%m-%d") AS HIRE_YMD
  FROM DOCTOR
 WHERE MCDP_CD='CS' OR MCDP_CD='GS'
 ORDER BY HIRE_YMD DESC, DR_NAME

 -- 12세 이하인 여자 환자 목록 출력하기
SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, "NONE")
  FROM PATIENT
 WHERE AGE <=12 AND GEND_CD="W" 
 ORDER BY AGE DESC, PT_NAME

 -- 나이 정보가 없는 회원 수 구하기
SELECT COUNT(USER_ID) AS USERS
  FROM USER_INFO
 WHERE AGE IS NULL

 -- 강원도에 위치한 생산공장 목록 출력하기
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS
  FROM FOOD_FACTORY
 WHERE SUBSTRING_INDEX(ADDRESS, " ", 1)="강원도"
 ORDER BY FACTORY_ID

 -- 이름이 없는 동물의 아이디
SELECT ANIMAL_ID
  FROM ANIMAL_INS
 WHERE NAME IS NULL
 ORDER BY ANIMAL_ID
