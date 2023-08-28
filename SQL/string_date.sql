-- SUBSTRING 을 이용해서 원하는 만큼 데이터를 추출할 수 있었다
-- 카테고리 별 상품 개수 구하기
SELECT SUBSTRING(PRODUCT_CODE,1,2) AS CATERGORY, COUNT(PRODUCT_ID) AS PRODUCTS
  FROM PRODUCT
 GROUP BY CATERGORY
 ORDER BY CATERGORY

-- 결과의 데이터 포맷에 따라서 추출
 -- DATETIME에서 DATE로 형 변환
SELECT ANIMAL_ID, NAME, DATE_FORMAT(DATETIME,"%Y-%m-%d")
  FROM ANIMAL_INS
 ORDER BY ANIMAL_ID

-- IF 혹은 CASE WHEN 절 사용
 -- 중성화 여부 파악하기
SELECT ANIMAL_ID
     , NAME
     , IF(SEX_UPON_INTAKE LIKE "Spayed %" 
       OR SEX_UPON_INTAKE LIKE "Neutered %", "O","X") AS "중성화"
     # , (CASE 
     # WHEN SEX_UPON_INTAKE LIKE "Spayed %" 
     #   OR SEX_UPON_INTAKE LIKE "Neutered %" THEN SEX_UPON_INTAKE="O"
     # ELSE SEX_UPON_INTAKE="X"
     # END) AS SEX_UPON_INTAKE
  FROM ANIMAL_INS
 ORDER BY ANIMAL_ID

 -- IN
-- 루시와 엘라 찾기
SELECT ANIMAL_ID, NAME, SEX_UPON_INTAKE
  FROM ANIMAL_INS
 WHERE NAME IN ("Lucy", "Ella", "Pickle", "Rogan", "Sabrina", "Mitty")

-- 조건을 잘 정리할 것
 -- 조건별로 분류하여 주문상태 출력하기
SELECT ORDER_ID
     , PRODUCT_ID
     , DATE_FORMAT(OUT_DATE,"%Y-%m-%d") AS OUT_DATE
     , CASE
        WHEN
        DATE_FORMAT(OUT_DATE,"%m-%d")<="05-01"
            THEN
            "출고완료"
        WHEN
        DATE_FORMAT(OUT_DATE,"%m-%d")>"05-01"
            THEN
            "출고대기"
        WHEN
        OUT_DATE IS NULL
            THEN
            "출고미정" 
        END AS "출고여부"
  FROM FOOD_ORDER
 ORDER BY ORDER_ID ASC

 -- 1. 입양을 간 동물 -> 입양간 동물 정보 테이블에 있어야한다(기준이 됨)
-- 2. 보호 기간 = 입양일 - 보호 시작일 
-- 3. 보호 기간이 가장 긴 = 보호 기간 값이 가장 큰
-- 오랜 기간 보호한 동물(2)
SELECT AO.ANIMAL_ID, AO.NAME
  FROM ANIMAL_OUTS AO
LEFT JOIN ANIMAL_INS AI -- LEFT JOIN / JOIN 둘 다 가능 
    ON AO.ANIMAL_ID=AI.ANIMAL_ID
 WHERE AO.DATETIME IS NOT NULL
 ORDER BY (AO.DATETIME-AI.DATETIME) DESC
 LIMIT 2 

-- GROUP 별 STRING을 모두 합치려면 - GROUP_CONCAT
-- 우유와 요거트가 담긴 장바구니
SELECT CART_ID
  FROM CART_PRODUCTS
 GROUP BY CART_ID
HAVING GROUP_CONCAT(NAME) LIKE "%Milk%" 
   AND GROUP_CONCAT(NAME) LIKE "%Yogurt%"
 ORDER BY CART_ID

 -- 취소되지 않은 진료 예약 조회하기
# SELECT 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목
# 조건 2022년 4월 13일
#     취소되지 않은
#     흉부외과(CS) 진료 예약 내역
# 정렬 진료예약일시를 기준으로 오름차순
SELECT A.APNT_NO, P.PT_NAME, A.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD
  FROM APPOINTMENT A
  JOIN DOCTOR D
    ON A.MDDR_ID=D.DR_ID
  JOIN PATIENT P
    ON A.PT_NO=P.PT_NO
 WHERE DATE_FORMAT(A.APNT_YMD,"%Y-%m-%d")="2022-04-13"
   AND A.APNT_CNCL_YN="N"
   AND A.MCDP_CD="CS"
 ORDER BY A.APNT_YMD 

-- 자동차 대여 기록 별 대여 금액 구하기
-- 단계1. 날짜별로 대여비를 할인율 적용한 값을 계산한다.
SELECT HISTORY_ID -- 대여 기록 아이디
     , FLOOR(DAILY_FEE * (DATEDIFF(END_DATE, START_DATE) + 1) * (100 - COALESCE(DISCOUNT_RATE, 0)) / 100) FEE
     -- 대여비 계산
     , CAST(SUBSTR(DURATION_TYPE, 1, INSTR(DURATION_TYPE, '일 이상') - 1) AS SIGNED) boundary
     -- 적용할 퍼센트 범위
  FROM CAR_RENTAL_COMPANY_CAR car
  JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY rental -- 대여 날짜 필요
    ON car.CAR_ID = rental.CAR_ID
LEFT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN plan -- 할인율 필요
    ON car.CAR_TYPE = plan.CAR_TYPE 
   AND DATEDIFF(END_DATE, START_DATE) + 1 >= SUBSTR(DURATION_TYPE, 1, INSTR(DURATION_TYPE, '일 이상') - 1)
   -- 대여날이 할인율 날과 비교하여, 더 커야한다..?
 WHERE car.CAR_TYPE = '트럭'
-- 단계2. 위 코드를 FROM에 넣는다.
-- row_num를 생성
SELECT HISTORY_ID, FEE
     , ROW_NUMBER() OVER (
                 PARTITION BY HISTORY_ID ORDER BY boundary DESC) row_num
  FROM (
                SELECT HISTORY_ID
                     , FLOOR(DAILY_FEE * (DATEDIFF(END_DATE, START_DATE) + 1) * (100 - COALESCE(DISCOUNT_RATE, 0)) / 100) FEE
                     , CAST(SUBSTR(DURATION_TYPE, 1, INSTR(DURATION_TYPE, '일 이상') - 1) AS SIGNED) boundary
                  FROM CAR_RENTAL_COMPANY_CAR car
                  JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY rental 
                    ON car.CAR_ID = rental.CAR_ID
       LEFT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN plan
                    ON car.CAR_TYPE = plan.CAR_TYPE 
                       AND DATEDIFF(END_DATE, START_DATE) + 1 >= SUBSTR(DURATION_TYPE, 1, INSTR(DURATION_TYPE, '일 이상') - 1)
                 WHERE car.CAR_TYPE = '트럭') t
-- 3단계. row_num을 이용한 조건문
 SELECT HISTORY_ID, FEE
  FROM (
        SELECT HISTORY_ID, FEE
             , ROW_NUMBER() OVER (
                 PARTITION BY HISTORY_ID ORDER BY boundary DESC) row_num
          FROM (
                SELECT HISTORY_ID
                     , FLOOR(DAILY_FEE * (DATEDIFF(END_DATE, START_DATE) + 1) * (100 - COALESCE(DISCOUNT_RATE, 0)) / 100) FEE
                     , CAST(SUBSTR(DURATION_TYPE, 1, INSTR(DURATION_TYPE, '일 이상') - 1) AS SIGNED) boundary
                  FROM CAR_RENTAL_COMPANY_CAR car
                  JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY rental 
                    ON car.CAR_ID = rental.CAR_ID
       LEFT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN plan
                    ON car.CAR_TYPE = plan.CAR_TYPE 
                       AND DATEDIFF(END_DATE, START_DATE) + 1 >= SUBSTR(DURATION_TYPE, 1, INSTR(DURATION_TYPE, '일 이상') - 1)
                 WHERE car.CAR_TYPE = '트럭') t
        ) t
 WHERE row_num = 1
 ORDER BY FEE DESC, HISTORY_ID DESC