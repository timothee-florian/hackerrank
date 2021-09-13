-- https://www.hackerrank.com/challenges/interviews/problem
-- Need to make one one with group by
select c.contest_id, c.hacker_id, c.name, 
IFNULL(sum(total_submissions), 0) as total_submissions, IFNULL(sum(total_accepted_submissions), 0) as total_accepted_submissions,
IFNULL(sum(total_views), 0) as total_views, IFNULL(sum(total_unique_views), 0) as total_unique_views
from contests c 
join colleges co on c.contest_id = co.contest_id
join challenges ch on co.college_id = ch.college_id
left join (select challenge_id, sum(total_views) as total_views, sum(total_unique_views) as total_unique_views from View_Stats group by challenge_id) vs
on ch.challenge_id = vs.challenge_id
left join (select challenge_id, sum(total_submissions) as total_submissions, sum(total_accepted_submissions) as total_accepted_submissions from submission_stats group by challenge_id) ss
on ch.challenge_id = ss.challenge_id
group by c.contest_id, c.hacker_id, c.name
having total_submissions + total_accepted_submissions + total_views + total_unique_views > 0
order by c.contest_id