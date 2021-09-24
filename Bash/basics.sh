# https://www.hackerrank.com/challenges/bash-tutorials-lets-echo/problem
# print 
echo HELLO

# https://www.hackerrank.com/challenges/bash-tutorials---a-personalized-echo/problem
# read input
read name
echo "Welcome $name"

# https://www.hackerrank.com/challenges/bash-tutorials---looping-with-numbers/problem
# Loop
i=1
while [ $i -le 50 ]
do
    echo $i
    i=$((i+1))
done


# https://www.hackerrank.com/challenges/bash-tutorials---the-world-of-numbers/problem
# Arithmetic
read X
read Y
echo "$((X + Y))"
echo "$((X - Y))"
echo "$((X * Y))"
echo "$((X / Y))"
echo "$((X % Y))"


# https://www.hackerrank.com/challenges/bash-tutorials---more-on-conditionals/problem
# if elif else
read X
read Y
read Z

if [[ $X == $Y && $Y == $Z ]]
then
    echo 'EQUILATERAL';
elif [[ $X == $Y || $Y == $Z ]]
then
    echo 'ISOSCELES';
else
    echo 'SCALENE';
fi

# https://www.hackerrank.com/challenges/bash-tutorials---looping-and-skipping/problem
# loop if skip
i=1
while [ $i -le 99 ]
do
    let "modu = $i % 2"
    if [ $modu == 1 ]
    then
    echo $i
    fi
    
    i=$((i+1))
done