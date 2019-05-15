#!/usr/bin/env python
# http://www.rabbitmq.com/tutorials/tutorial-two-python.html
import pika
import sys
credentials = pika.PlainCredentials('oleg', '123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='node1', credentials=credentials))
channel = connection.channel()

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key='task_queue',
                      body=message
)
print(" [x] Sent {0}".format(message))
connection.close()
