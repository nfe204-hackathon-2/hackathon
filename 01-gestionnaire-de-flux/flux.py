#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 18:54:55 2017

@author: yvan
"""

from kafka import KafkaProducer
from kafka.errors import KafkaError
import msgpack
producer = KafkaProducer(bootstrap_servers=['163.173.230.141:9092','163.173.230.137:9092'])

# Asynchronous by default
#future = producer.send('my-topic', b'raw_bytes')

# Block for 'synchronous' sends
#try:
#    record_metadata = future.get(timeout=10)
#except KafkaError:
#    # Decide what to do if produce request failed...
#    log.exception()
#    pass

# Successful result returns assigned partition and offset
#print (record_metadata.topic)
#print (record_metadata.partition)
#print (record_metadata.offset)

# produce keyed messages to enable hashed partitioning
#producer.send('my-topic', key=b'foo', value=b'bar')

# encode objects via msgpack
#producer = KafkaProducer(value_serializer=msgpack.dumps)
#producer.send('msgpack-topic', {'key': 'value'})

# produce json messages
#producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
#producer.send('json-topic', {'key': 'value'})

import json
import time
with open('/tmp/extract_tweets_5000000.json', 'r') as f:
     data = json.load(f)
# produce asynchronously
for i in range(50000):
    print("Step {}".format(i))
    time.sleep(5)
    for j in range(100):
        msg = json.dumps(data[i * 100 + j])
        print("Message : {}".format(msg))
        producer.send('my-topic', "{}".format(msg).encode("utf-8"))

# block until all async messages are sent
producer.flush()
print("DONE")
# configure multiple retries
# producer = KafkaProducer(retries=5)
