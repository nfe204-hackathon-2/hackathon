# Divers

## Exemple
https://spark.apache.org/docs/latest/quick-start.html

## Pour construire le projet
```
$ sbt package
```

## Pour lancer le projet
```
../../Documents/cnam/nfe204/spark-2.2.0-bin-hadoop2.7/bin/spark-submit \
        --packages org.apache.spark:spark-streaming-kafka-0-10_2.11:2.2.0,com.typesafe.play:play-json_2.11:2.6.0 \
        --class "SimpleApp" target/scala-2.11/simple-project_2.11-1.0.jar localhost:2181 my-topic
```
