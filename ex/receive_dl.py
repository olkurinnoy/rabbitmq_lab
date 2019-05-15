#!/usr/bin/env python                                                                                                                                                                                                                                                                                                                                               [15/19]
# http://www.rabbitmq.com/tutorials/tutorial-two-python.html
import time
import pika
credentials = pika.PlainCredentials('oleg', '123456')

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='node1', credentials = credentials))
channel = connection.channel()

channel.exchange_declare(exchange='dlx', type='direct')

channel.queue_declare(queue='dl',
                      arguments={
                              'x-message-ttl': 5000,
                              'x-dead-letter-exchange': 'amq.direct',
                              'x-dead-letter-routing-key': 'task_queue'
                      })

channel.queue_bind(exchange='dlx', queue='dl')

print ' [*] Waiting for dead-letters. To exit press CTRL+C'
