# Write your MySQL query statement below
SELECT seller_id FROM Sales
GROUP BY seller_id
HAVING SUM(price) = (
                SELECT max(total_price) from
                (
                    SELECT seller_id, sum(price) as total_price from
                    Sales GROUP BY seller_id
                ) as max_sale
)
Order by seller_id asc