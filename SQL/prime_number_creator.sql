/*
https://www.hackerrank.com/challenges/print-prime-numbers/problem
*/

delimiter $$
create procedure getPrime(IN n int, OUT result varchar(10000))
Begin
declare j, i, flag int;  
set j:=2; 
set result:=''; 
while(j<n) do
set i:=2;
set flag:=0;

while(i<=j) do
if(j%i=0)then
set flag:=flag+1;
end if;
set i:=i+1;
end while;

if (flag=1) then
set result:=concat(result, j, '&'); 
end if ;
set j:=j+1; 
end while;

End
$$

call getPrime(1000, @result);
select substr(@result, 1, length(@result)-1);