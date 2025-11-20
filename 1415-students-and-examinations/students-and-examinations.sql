# Write your MySQL query statement below
-- select * from Students;

-- select * from Subjects;

-- select * from Examinations;

-- select * from Students s left join Examinations e
-- on s.student_id = e.student_id
-- order by s.student_id

-- select student_id, subject_name, COUNT(*) AS attended_exams
-- from Examinations
-- group by student_id, subject_name;

select s.student_id, s.student_name, sub.subject_name, count(e.subject_name) as attended_exams from Students s
cross join Subjects sub
left join Examinations e
on s.student_id = e.student_id and 
   sub.subject_name = e.subject_name
group by s.student_id, s.student_name, sub.subject_name
order by s.student_id, sub.subject_name