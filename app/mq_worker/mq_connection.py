import pika

# RabbitMQ Setup
QUEUE_1 = 'message_queue_1'
QUEUE_2 = 'message_queue_2'

def get_rabbitmq_channel():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_1)
    channel.queue_declare(queue=QUEUE_2)

    return channel, connection