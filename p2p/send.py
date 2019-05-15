#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('oleg', '123456')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='node1',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello2', durable = True)


message = ' '.join(sys.argv[1:])
channel.basic_publish(exchange='', routing_key='hello2', body=message)


print(" [x] Sent {0}".format(message))
connection.close()

