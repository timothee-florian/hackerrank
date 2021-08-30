/*https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=false*/
select s4.hacker_id, h.name, s4.count_challenge
from
(
  select s3.hacker_id, s3.count_challenge
  from
  (
    select hacker_id, count(challenge_id) as count_challenge from Challenges group by hacker_id
  ) s3
  where s3.count_challenge in
  (
    select s2.count_challenge
    from (select count(challenge_id) as count_challenge from Challenges group by hacker_id) s2
    group by count_challenge
    having count(s2.count_challenge) = 1
  )
  or
  s3.count_challenge =
    (select max(s1.count_challenge) as max_c from (select count(challenge_id) as count_challenge from Challenges group by hacker_id) s1)
) s4, Hackers h
where h.hacker_id = s4.hacker_id
order by s4.count_challenge desc, s4.hacker_id
