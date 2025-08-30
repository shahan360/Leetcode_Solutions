# Write your MySQL query statement below
-- select * from Person

select firstName, lastName, city, state from Person p
left join Address a
on a.personId = p.personId