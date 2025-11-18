# Write your MySQL query statement below
SELECT DATE_FORMAT(trans_date, '%Y-%m') as month, country, count(id) as trans_count,SUM(if(state = 'approved', 1,0)) as approved_count, sum(amount) as trans_total_amount, SUM(if(state = 'approved', amount,0)) as approved_total_amount from Transactions
group by month, country