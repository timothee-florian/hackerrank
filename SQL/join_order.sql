/*
https://www.hackerrank.com/challenges/placements/problem
*/

select self_salary.name from
(select students.name, friends.id, friends.friend_id, packages.salary 
from friends, packages, students where friends.id = packages.id and students.id = friends.id) self_salary
join 
(select friends.id, friends.friend_id, packages.salary 
from friends, packages where friends.friend_id = packages.id) friend_salary

on self_salary.id = friend_salary.id and self_salary.salary < friend_salary.salary
order by friend_salary.salary