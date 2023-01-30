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