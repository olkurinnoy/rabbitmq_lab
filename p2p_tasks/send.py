#!/usr/bin/env python
import pika
import sys
import time

credentials = pika.PlainCredentials('oleg', '123456')



connection = pika.BlockingConnection(pika.ConnectionParameters(host='node1',credentials=credentials))

channel = connection.channel()
channel.queue_declare(queue='hello2', durable = True)

'''
channel.queue_bind(exchange='amq.direct', queue = 'hello7')

ch1 = connection.channel()
ch1.confirm_delivery()

delay_channel.queue_declare(queue='hello_delay', durable=True,  arguments={
  'x-message-ttl' : 5000, 
  'x-dead-letter-exchange' : 'amq.direct',
  'x-dead-letter-routing-key' : 'hello' 
})
'''
	
for i in range(10):
	channel.basic_publish(exchange='', routing_key='hello6', body=str(i))
	print(" [x] Sent {0}".format(i))
	#time.sleep(1)

connection.close()

