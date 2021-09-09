/*
https://www.hackerrank.com/challenges/sql-projects/problem
*/
select start_date, min(end_date)
from
    (select start_date from Projects where start_date not in (select end_date from Projects)) a,
    (select end_date from Projects where end_date not in (select start_date from Projects)) b
where start_date < end_date
group by start_date
order by datediff(min(end_date), start_date), start_date