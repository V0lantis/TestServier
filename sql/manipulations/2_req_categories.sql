SELECT
    transaction.client_id,
    SUM(CASE WHEN product_nomenclature.product_type = 'MEUBLE' THEN transaction.prod_qty ELSE 0 END) AS ventes_meubles,
    SUM(CASE WHEN product_nomenclature.product_type = 'DECO' THEN transaction.prod_qty ELSE 0 END) AS ventes_deco
FROM transaction LEFT JOIN product_nomenclature
ON transaction.prod_id=product_nomenclature.product_id
WHERE transaction.dt BETWEEN DATE '2019-01-01' AND DATE '2019-12-31'
AND product_type IN ('MEUBLE', 'DECO')
GROUP BY client_id