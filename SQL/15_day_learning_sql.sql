create table submissions ( submission_date date, submission_id int, hacker_id int, score int );

insert into submissions values 
('2016-03-01', 8494, 20703, 0), 
('2016-03-01', 23965, 79722, 60), 
('2016-03-01', 23965, 79722, 60), 
('2016-03-01', 30173, 36396, 70), 
('2016-03-02', 34928, 20703, 0), 
('2016-03-02', 38740, 15758, 60), 
('2016-03-02', 42769, 79722, 60), 
('2016-03-02', 44364, 79722, 60), 
('2016-03-03', 45440, 20703, 0), 
('2016-03-03', 49050, 36396, 70), 
('2016-03-03', 50273, 79722, 5), 
('2016-03-04', 50344, 20703, 0), 
('2016-03-04', 51360, 44065, 90), 
('2016-03-04', 54404, 53473, 65), 
('2016-03-04', 61533, 79722, 45), 
('2016-03-05', 72852, 20703,0), 
('2016-03-05',74546, 38289, 0), 
('2016-03-05', 76487, 62529, 0), 
('2016-03-05',82439, 36396, 10), 
('2016-03-05', 9006, 36396, 40), 
('2016-03-06', 90404, 20703, 0); 

create table hackers ( hacker_id int, name varchar(255) ); insert into hackers values 
(15758, 'Rose'), 
(20703, 'Angela'), 
(36396, 'Frank'), 
(38289, 'Patrick'), 
(44065, 'Lisa'), 
(53473, 'Kimberly'), 
(62529, 'Bonnie'), 
(79722, 'Michael');


select 
submission_date ,

( SELECT COUNT(distinct hacker_id)  
 FROM Submissions s2  
 WHERE s2.submission_date = s1.submission_date AND    
 (SELECT COUNT(distinct s3.submission_date) FROM      
 Submissions s3 WHERE 
 s3.hacker_id = s2.hacker_id AND 
 s3.submission_date <= s2.submission_date) = dateDIFF(s2.submission_date , '2016-03-01')+1) as count_ ,
 
 (select s2.hacker_id from submissions s2 where s2.submission_date = s1.submission_date 
 group by s2.hacker_id order by count(*) desc, hacker_id limit 1  ) as h_id,
 
 (select name from hackers h where h.hacker_id = h_id)
 
from 
(select distinct submission_date from submissions) s1
group by submission_date;
