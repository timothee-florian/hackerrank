// https://www.hackerrank.com/challenges/fp-filter-array/problem
// filter
def f(delim:Int,arr:List[Int]):List[Int] ={
    return arr.filter(_ < delim)
}