name := "Simple Project"

version := "1.0"

scalaVersion := "2.11.8"

libraryDependencies += "org.apache.spark" %% "spark-core" % "2.2.0" % Provided
libraryDependencies += "org.apache.spark" %% "spark-streaming" % "2.2.0"  % Provided
libraryDependencies += "org.apache.spark" %% "spark-streaming-kafka-0-10" % "2.2.0"

libraryDependencies += "com.typesafe.play" %% "play-json" % "2.6.0"