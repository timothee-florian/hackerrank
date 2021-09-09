/*
https://www.hackerrank.com/challenges/symmetric-pairs/problem
*/
SELECT f1.X, f1.Y FROM Functions f1, Functions f2
WHERE f1.X = f2.Y and f1.Y = f2.X and f1.X <= f1.Y
group by f1.X, f1.Y
having count(f1.X) > 1 or f1.X <> f1.Y
ORDER BY f1.X;