SELECT dt AS "date", sum(prod_qty * prod_price) AS ventes
FROM transaction
WHERE dt between DATE '2019-01-01' AND DATE '2019-12-31'
GROUP BY dt
ORDER BY dt;

