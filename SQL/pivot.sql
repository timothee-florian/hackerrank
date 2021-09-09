/*
https://www.hackerrank.com/challenges/occupations/problem
*/

set @ra=0, @rd=0, @rp=0, @rs=0;
select min(Doctor), min(Professor), min(Singer), min(Actor)
from(
  select case when Occupation='Doctor' then (@rd:=@rd+1)
            when Occupation='Professor' then (@rp:=@rp+1)
            when Occupation='Singer' then (@rs:=@rs+1)
            when Occupation='Actor' then (@ra:=@ra+1) end as RowNumber,
    case when Occupation='Doctor' then Name end as Doctor,
    case when Occupation='Professor' then Name end as Professor,
    case when Occupation='Singer' then Name end as Singer,
    case when Occupation='Actor' then Name end as Actor
  from Occupations
    order by Name 
    ) temp
    group by RowNumber;