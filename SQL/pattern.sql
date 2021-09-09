/*
https://www.hackerrank.com/challenges/draw-the-triangle-2/problem
*/
set @r=0, @n=20;
select repeat('* ', @r := @r + 1) from information_schema.tables where @r < @n;