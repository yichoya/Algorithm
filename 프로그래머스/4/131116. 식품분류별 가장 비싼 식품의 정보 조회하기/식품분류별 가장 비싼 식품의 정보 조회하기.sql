SELECT F.CATEGORY, F.PRICE MAX_PRICE, F.PRODUCT_NAME
FROM FOOD_PRODUCT F JOIN (
    SELECT CATEGORY, MAX(PRICE) PRICE
    FROM FOOD_PRODUCT
    GROUP BY CATEGORY
) sub ON F.CATEGORY = sub.CATEGORY
WHERE F.CATEGORY IN ('과자', '국', '김치', '식용유')
    AND F.PRICE = sub.PRICE
ORDER BY F.PRICE DESC