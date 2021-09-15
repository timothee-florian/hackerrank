object Solution {
    
     def fibonacci(x:Int):Int = {
        if (x==1 || x == 2) return x -1
        return fibonacci(x - 1) + fibonacci(x -2)
     }

    def main(args: Array[String]) {
        /** This will handle the input and output**/
        val readInt = scala.io.StdIn.readInt
        println(fibonacci(readInt))

    }
}