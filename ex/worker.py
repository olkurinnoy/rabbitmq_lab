#!/usr/bin/env python
# http://www.rabbitmq.com/tutorials/tutorial-two-python.html
import pika
import time
import random
credentials = pika.PlainCredentials('oleg', '123456')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='node1', credentials = credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue',
                      arguments={
                          'x-message-ttl' : 1000,
                          'x-dead-letter-exchange' : 'dlx',
                          'x-dead-letter-routing-key' : 'dl'
                      }
)

channel.queue_bind(exchange='amq.direct', queue='task_queue')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    print " [x] Properties %r" % (properties,)
    #if random.random() < 0.5:
    if False:
        ch.basic_ack(delivery_tag = method.delivery_tag)
        time.sleep(5)
        print " [x] Done"
    else:
        if properties.headers.get('x-death') == None or properties.headers['x-retry-count'] < 5:
            ch.basic_reject(delivery_tag = method.delivery_tag, requeue=False)
            print " [x] Rejected"
        else:
            ch.basic_ack(delivery_tag=method.delivery_tag)
            print " [x] Timed out"

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,
                      queue='task_queue')

channel.start_consuming()
