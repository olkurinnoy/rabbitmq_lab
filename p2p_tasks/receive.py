import pika

credentials = pika.PlainCredentials('oleg', '123456')
connection = pika.BlockingConnection(
	pika.ConnectionParameters(host='node1',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='hello2', durable=True)


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(
    queue='hello2', on_message_callback=callback, auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
