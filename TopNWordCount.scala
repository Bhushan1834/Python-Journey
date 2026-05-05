import org.apache.spark.sql.SparkSession

object SparkWordCount {
  def main(args: Array[String]): Unit = {
    // 1. Initialize the SparkSession
    // In a local environment, we set master to 'local[*]' to use all available cores
    val spark = SparkSession.builder()
      .appName("TopN Word Count")
      .master("local[*]")
      .getOrCreate()

    // 2. Set the path to the text file and the N value
    val inputPath = "input.txt"
    val N = 5

    try {
      // 3. Read the text file into an RDD
      val textFile = spark.sparkContext.textFile(inputPath)

      // 4. Perform Word Count logic
      val wordCounts = textFile
        .flatMap(line => line.split("\\W+"))     // Split by non-word characters (Tokenization)
        .map(word => word.toLowerCase)            // Normalize to lowercase
        .filter(word => word.nonEmpty)            // Remove empty strings
        .map(word => (word, 1))                   // MAP: (word, 1)
        .reduceByKey(_ + _)                       // REDUCE: sum frequencies

      // 5. Get Top-N most frequent words
      // We swap (word, count) to (count, word) for sorting, then take top N
      val topNWords = wordCounts
        .map(pair => (pair._2, pair._1))          // Swap for sorting
        .sortByKey(ascending = false)             // Sort by frequency descending
        .take(N)                                  // Get top N

      // 6. Print the results
      println(s"\n--- Top $N Most Frequent Words ---")
      topNWords.foreach { case (count, word) =>
        println(f"$word%-10s : $count")
      }

    } catch {
      case e: Exception => println(f"Error executing Spark job: ${e.getMessage}")
    } finally {
      // 7. Stop the SparkSession
      spark.stop()
    }
  }
}
