/*
https://www.hackerrank.com/challenges/harry-potter-and-wands/problem
*/

select id, age, w1.coins_needed, w1.power
from 
(select id, code, coins_needed, power from Wands w) w1
join
(
    select  w.code, age, min(coins_needed) as coins_needed, power from Wands w 
    join 
    (select code, age from Wands_Property where is_evil = 0) wp
    on w.code = wp.code
    group by age, power , w.code
) w2
on w1.code = w2.code and w1.power = w2.power and w1.coins_needed = w2.coins_needed
order by w1.power desc, age desc