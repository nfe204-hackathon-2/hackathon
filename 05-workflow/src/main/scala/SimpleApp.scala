import org.apache.kafka.common.serialization.StringDeserializer
import org.apache.spark.SparkConf
import org.apache.spark.streaming.dstream.DStream
import org.apache.spark.streaming.kafka010.ConsumerStrategies.Subscribe
import org.apache.spark.streaming.kafka010.LocationStrategies.PreferConsistent
import org.apache.spark.streaming.kafka010._
import org.apache.spark.streaming.{Seconds, StreamingContext}
import play.api.libs.json._

object SimpleApp {
  def main(args: Array[String]) {
    if (args.length < 2) {
      System.err.println(
        s"""
           |Usage: DirectKafkaWordCount <brokers> <topics>
           |  <brokers> is a list of one or more Kafka brokers
           |  <topics> is a list of one or more kafka topics to consume from
           |
        """.stripMargin)
      System.exit(1)
    }

    val Array(brokers, topics: String) = args

    // Create context with 2 second batch interval
    val sparkConf = new SparkConf().setAppName("DirectKafkaWordCount")
    val ssc = new StreamingContext(sparkConf, Seconds(2))

    val kafkaParams = Map[String, Object](
      "bootstrap.servers" -> "localhost:9092,anotherhost:9092",
      "key.deserializer" -> classOf[StringDeserializer],
      "value.deserializer" -> classOf[StringDeserializer],

      "group.id" -> "use_a_separate_group_id_for_each_stream",
      "auto.offset.reset" -> "latest",
      "enable.auto.commit" -> (false: java.lang.Boolean)
    )


    val stream = KafkaUtils.createDirectStream[String, String](
      ssc,
      PreferConsistent,
      Subscribe[String, String](Seq(topics), kafkaParams)
    )

    System.out.println("#######################")
    val c = stream
      .map(_.value())
      .map(Json.parse)
      .map((json: JsValue) => (json \ "text").get.toString())
      .flatMap(text => text.split(" ").toSeq)
      .map(w => (w, 1))
      .reduceByKeyAndWindow((a, b) => a + b, Seconds(30))
    //.reduceByKeyAndWindow({ (a, b) => a + b }, Seconds(30), Seconds(10))
    c.print()
    c.context.start()
    System.out.println("Starting")
    c.context.awaitTermination()
    System.out.println("Done")
    // val unit: DStream[(String, Map[String, Object])] = stream.map(record => (record.key, record.value))
    /*

        val sqlContext = new SQLContext(ssc.sparkContext)
    stream
      .reduceByWindow((a, b) => a, Seconds(30), Seconds(10))
      .foreachRDD(
        (rdd: RDD[ConsumerRecord[String, Map[String, Object]]]) => {
          val dataFrame = sqlContext.read.json(rdd.map(x => x.key())) //converts json to DF
          //do your operations on this DF. You won't even require a model class.
        })
     */
  }
}
