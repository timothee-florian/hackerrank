// https://www.hackerrank.com/challenges/fp-filter-array/problem
// filter
def f(delim:Int,arr:List[Int]):List[Int] ={
    return arr.filter(_ < delim)
}

// https://www.hackerrank.com/challenges/fp-array-of-n-elements/problem
// Create list of n elements, had to define readInt
object Solution extends App {

    def f(num:Int) : List[Int] = {
        val list = List.range(0, num)

        return list
    }

    val readInt = scala.io.StdIn.readInt
    println(f(readInt))
}

// https://www.hackerrank.com/challenges/fp-sum-of-odd-elements/problem
// sum odd numbers
def f(arr:List[Int]):Int = {
    return arr.filter(x => x%2 != 0).reduce(_ + _)
}