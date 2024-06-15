import json
import os
import time

import pika

import render_ffmpeg


def print_log(*args):
    print(' '.join([str(arg) for arg in args]), end="\n")


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=os.environ['RABBITMQ_HOST']))
    channel = connection.channel()

    channel.queue_declare(queue='render')

    def callback(ch, method, properties, body):
        data = json.loads(body)
        print_log(data)
        render_ffmpeg.render(data)

    channel.basic_consume(queue='render', on_message_callback=callback, auto_ack=True)

    channel.start_consuming()


if __name__ == '__main__':
    time.sleep(10)
    main()