import pika
import sys
import pickle
import time

credentials = pika.PlainCredentials('oleg', '123456')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='node1',credentials=credentials))
channel = connection.channel()


channel.queue_declare(queue='hello')


class human:
	def __init__(self, age = 10, name = 'Oleg'):
		self.age = age
		self.name = name

for i in range(10):
	name = 'Oleksii ' + str(i)
	h1 = human(11, name)
	time.sleep(1)
	mess = pickle.dumps(h1, protocol = 1)
	channel.basic_publish(exchange = '', routing_key = 'hello', body = mess)
	print(" [x] Sent {0}".format(name))

connection.close()

