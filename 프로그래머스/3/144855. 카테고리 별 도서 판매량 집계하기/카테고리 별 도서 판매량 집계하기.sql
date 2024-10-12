SELECT CATEGORY, SUM(SALES) TOTAL_SALES
FROM BOOK_SALES BS JOIN BOOK B ON BS.BOOK_ID = B.BOOK_ID
-- WHERE BS.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
WHERE BS.SALES_DATE like '2022-01%'
GROUP BY CATEGORY
ORDER BY CATEGORY