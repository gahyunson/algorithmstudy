-- sub query 적용
-- 가격이 제일 비싼 식품의 정보 출력하기
SELECT *
  FROM FOOD_PRODUCT
 WHERE PRICE=(SELECT MAX(PRICE) FROM FOOD_PRODUCT)
