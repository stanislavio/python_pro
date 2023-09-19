import pika


def callback(ch, method, properties, body):
    print(ch)
    print(method)
    print(properties)
    print(f" [x] Received {body}")


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='my_first_queue')

channel.basic_consume(
    queue='my_first_queue', on_message_callback=callback, auto_ack=True
)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
