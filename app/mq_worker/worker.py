import threading
from app.mq_worker.mq_connection import QUEUE_1, QUEUE_2, get_rabbitmq_channel


# Worker function for Queue 1
def message_worker_queue_1():
    channel, connection = get_rabbitmq_channel()

    def callback(ch, method, properties, body):
        content = body.decode('utf-8')
        processed_content = content + " from queue 1!"
        save_message_to_db(processed_content)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=QUEUE_1, on_message_callback=callback)
    print("Worker for queue 1 started, waiting for messages...")
    channel.start_consuming()

# Worker function for Queue 2
def message_worker_queue_2():
    channel, connection = get_rabbitmq_channel()

    def callback(ch, method, properties, body):
        content = body.decode('utf-8')
        processed_content = content + " from queue 2!"
        save_message_to_db(processed_content)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_consume(queue=QUEUE_2, on_message_callback=callback)
    print("Worker for queue 2 started, waiting for messages...")
    channel.start_consuming()

# Function to save message to database
def save_message_to_db(content):
    # db = SessionLocal()
    # new_message = Message(content=content)
    print(f'Save message to DB [{content}]')
    # db.add(new_message)
    # db.commit()
    # db.close()

# Start worker threads for both queues
def start_workers():
    worker_thread_1 = threading.Thread(target=message_worker_queue_1)
    worker_thread_1.daemon = True
    worker_thread_1.start()

    worker_thread_2 = threading.Thread(target=message_worker_queue_2)
    worker_thread_2.daemon = True
    worker_thread_2.start()
