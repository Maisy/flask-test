from flask import request, jsonify
from flask import Blueprint, jsonify
from app.mq_worker.mq_connection import QUEUE_1, QUEUE_2, get_rabbitmq_channel

messages = Blueprint('messages', __name__)

@messages.route('/index', methods=['POST'])
def create_message_queue_1():
    content = request.json.get('content')
    if not content:
        return jsonify({'error': 'Message content is required'}), 400

    channel, connection = get_rabbitmq_channel()
    channel.basic_publish(exchange='', routing_key=QUEUE_1, body=content)
    connection.close()
    
    return jsonify({'message': 'Message enqueued to queue 1 successfully'}), 200


@messages.route('/docs', methods=['POST'])
def create_message_queue_2():
    content = request.json.get('content')
    if not content:
        return jsonify({'error': 'Message content is required'}), 400

    channel, connection = get_rabbitmq_channel()
    channel.basic_publish(exchange='', routing_key=QUEUE_2, body=content)
    connection.close()
    
    return jsonify({'message': 'Message enqueued to queue 2 successfully'}), 200


