# Write your MySQL query statement below
select employee_id 
    from Employees 
    where 
    salary < 30000
    and manager_id is not null
    and manager_id not in (SELECT employee_id FROM Employees)
    ORDER BY
    employee_id;