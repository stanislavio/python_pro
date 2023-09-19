import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='my_first_queue')

channel.basic_publish(
    exchange='', routing_key='my_first_queue', body='Hello, fqlewbf!1'.encode()
)

print(" [x] Sent 'Hello, RabbitMQ!'")

connection.close()

