# Write your MySQL query statement below
-- from Product table select product_id and product_name where sale date lies between 2019-01-01 and 2019-03-31 inclusive

SELECT p.product_id, p.product_name
FROM Product p
INNER JOIN Sales s
ON p.product_id = s.product_id
GROUP BY p.product_id, p.product_name
HAVING
    MAX(s.sale_date) <= '2019-03-31' -- no sales after Q1 2019
    AND MIN(s.sale_date) >= '2019-01-01' -- no sales before Q1 2019
