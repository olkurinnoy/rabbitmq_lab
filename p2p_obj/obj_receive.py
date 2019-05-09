import pika
import sys
import pickle

credentials = pika.PlainCredentials('oleg', '123456')
connection = pika.BlockingConnection(
	pika.ConnectionParameters(host='node1',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')

class human:
    def __init__(self, age=10, name='Oleg'):
        self.age = age
        self.name = name

def callback(ch, method, properties, body):
    obj = pickle.loads(body)
    print(" [x] Received %r" % obj.name)


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
