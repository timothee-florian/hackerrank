object Solution {
    
    def pascal(arr: List[Int], k: Int) {
        println(arr.mkString(" "))
        val zero: List[Int] = List(0)
        val arr1 = List.concat(zero, arr)
        val arr2: List[Int] = List.concat(arr, zero)
        val arr0 = arr1.zip(arr2).map(t => t._1 + t._2)
        if (arr0.size <= k) {pascal(arr0, k)}
    }

    def main(args: Array[String]) {
    val readInt = scala.io.StdIn.readInt
    pascal(List(1),readInt)
        
    }
}
