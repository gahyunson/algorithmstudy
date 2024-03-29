-- DATE format 확인해야함!
-- 조건에 맞는 도서와 저자 리스트 출력하기
SELECT BOOK.BOOK_ID, AUTHOR.AUTHOR_NAME, DATE_FORMAT(BOOK.PUBLISHED_DATE, "%Y-%m-%d") AS PUBLISHED_DATE
  FROM BOOK 
  JOIN AUTHOR
    ON BOOK.AUTHOR_ID=AUTHOR.AUTHOR_ID 
 WHERE BOOK.CATEGORY="경제"
 ORDER BY BOOK.PUBLISHED_DATE

 -- 상품 별 오프라인 매출 구하기
SELECT PRODUCT_CODE, SUM(PRICE*SALES_AMOUNT) AS SALES
  FROM PRODUCT AS P, OFFLINE_SALE AS OS
 WHERE P.PRODUCT_ID=OS.PRODUCT_ID
 GROUP BY PRODUCT_CODE
 ORDER BY SALES DESC, PRODUCT_CODE

-- 입양간 기록 중, 입양온 기록이 없는 자료는?
-- 없어진 기록 찾기
-- 방법1.
SELECT AO.ANIMAL_ID, AO.NAME
  FROM ANIMAL_OUTS AO
LEFT JOIN ANIMAL_INS AI
       ON AO.ANIMAL_ID=AI.ANIMAL_ID
 WHERE AI.ANIMAL_ID IS NULL
ORDER BY AO.ANIMAL_ID
-- 방법2.
-- LEFT JOIN 차집합으로 사용 
SELECT AO.ANIMAL_ID, AO.NAME
  FROM ANIMAL_OUTS AO
LEFT JOIN ANIMAL_INS AI
    ON AO.ANIMAL_ID=AI.ANIMAL_ID
 WHERE AI.ANIMAL_ID IS NULL

 -- DATETIME 이 더 빠른 값은 상대적으로 더 적은 값이다!
-- 있었는데요 없었습니다
SELECT AI.ANIMAL_ID, AI.NAME
  FROM ANIMAL_INS AI
  JOIN ANIMAL_OUTS AO
    ON AI.ANIMAL_ID=AO.ANIMAL_ID -- 외래키
 WHERE AI.DATETIME > AO.DATETIME -- 보호시작일(AI)보다 입양일(AO)이 더 빠른
 ORDER BY AI.DATETIME

-- LEFT JOIN 하는 이유
-- ANIMAL_INS = 동물 보호소에 있는 동물 정보
-- ANIMAL_OUTS = 입양보낸 동물 정보
-- 1. 입양가지 않은 동물의 정보는 ANIMAL_OUTS에 없다.
-- 2. 그러므로 입양가지 않은 동물은 모두 ANIMAL_INS에 존재한다.
-- JOIN ON 은 A, B 집합의 교집합 정보를 추출해준다.
-- LEFT JOIN은 A에서 A,B의 교집합 정보를 제외한 정보를 추출해준다.
-- 오랜 기간 보호한 동물(1)
SELECT AI.NAME, AI.DATETIME
  FROM ANIMAL_INS AI
LEFT JOIN ANIMAL_OUTS AO
    ON AI.ANIMAL_ID=AO.ANIMAL_ID
 WHERE AO.DATETIME IS NULL
 ORDER BY AI.DATETIME
 LIMIT 3

 -- 보호소에서 중성화한 동물
 -- 어떤 데이터가 중성화하고 안한것인지 파악해야한다.
-- Spayed 중성화됨
-- Intact 중성화안됨
-- Neutered 보호소에서 중성화함
-- SELECT AO.ANIMAL_ID, AO.ANIMAL_TYPE, AO.NAME,  AI.SEX_UPON_INTAKE, AO.SEX_UPON_OUTCOME
SELECT AO.ANIMAL_ID, AO.ANIMAL_TYPE, AO.NAME
  FROM ANIMAL_OUTS AO
LEFT JOIN ANIMAL_INS AI
       ON AO.ANIMAL_ID=AI.ANIMAL_ID
 WHERE (AO.SEX_UPON_OUTCOME LIKE "Neutered%" 
        OR AO.SEX_UPON_OUTCOME LIKE "Spayed%")
   AND (AI.SEX_UPON_INTAKE LIKE "Intact%")
-- AI에서 중성화 안한 경우 & AO 에서 중성화 한 경우
 ORDER BY AO.ANIMAL_ID

-- ORDERY BY 잊지 말것
 -- 그룹별 조건에 맞는 식당 목록 출력하기
# SELECT 회원 이름, 리뷰 텍스트, 리뷰 작성일
#   FROM MEMBER_PROFILE와 REST_REVIEW 
#  WHERE 리뷰를 가장 많이 작성한
#  ORDER BY 리뷰 작성일을 기준으로 오름차순, 리뷰 텍스트를 기준으로 오름차순
SELECT MR.MEMBER_NAME, RR.REVIEW_TEXT, DATE_FORMAT(RR.REVIEW_DATE,"%Y-%m-%d") REVIEW_DATE
  FROM MEMBER_PROFILE MR
  JOIN REST_REVIEW RR
    ON MR.MEMBER_ID=RR.MEMBER_ID
 WHERE MR.MEMBER_ID=(SELECT RR.MEMBER_ID
                       FROM REST_REVIEW RR
                      GROUP BY RR.MEMBER_ID
                      ORDER BY COUNT(*) DESC
                      LIMIT 1)
 ORDER BY REVIEW_DATE, REVIEW_TEXT

 -- 주문량이 많은 아이스크림들 조회하기
# SELECT 상위 3개의 맛을 조회
SELECT FLAVOR
FROM (SELECT *
        FROM FIRST_HALF F
       UNION
      SELECT *
        FROM JULY J) JJ
GROUP BY FLAVOR
ORDER BY SUM(TOTAL_ORDER) DESC
LIMIT 3