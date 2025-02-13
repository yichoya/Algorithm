SELECT R.FOOD_TYPE, R.REST_ID, R.REST_NAME, R.FAVORITES
FROM REST_INFO R, (
    SELECT FOOD_TYPE, MAX(FAVORITES) MAX_FAVORITES
    FROM REST_INFO
    GROUP BY FOOD_TYPE
    ) MF
WHERE R.FOOD_TYPE = MF.FOOD_TYPE 
    AND R.FAVORITES = MF.MAX_FAVORITES
ORDER BY FOOD_TYPE DESC