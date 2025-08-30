# Write your MySQL query statement below
with counts as (
    select email,count(*) as cnt 
    from Person
    group by email)
select email as Email from counts where cnt > 1