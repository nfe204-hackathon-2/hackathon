#!/bin/sh

set -x

KAFKA_GZ=kafka_2.11-1.0.0.tgz
KAFKA_DIR=$PWD/kafka_2.11-1.0.0

if [ ! -e $KAFKA_GZ ]
then
	echo "Telechargement de $KAFKA_GZ"
	wget http://www-eu.apache.org/dist/kafka/1.0.0/$KAFKA_GZ
	tar -xf $KAFKA_GZ
fi

$KAFKA_DIR/bin/zookeeper-server-start.sh $KAFKA_DIR/config/zookeeper.properties &

sleep 10
$KAFKA_DIR/bin/kafka-server-start.sh $KAFKA_DIR/config/zookeeper.properties

