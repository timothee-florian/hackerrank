# https://www.hackerrank.com/challenges/bash-tutorials-lets-echo/problem
# print 
echo HELLO
########################################################################

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