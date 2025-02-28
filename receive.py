import pika, sys, os


def main():

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='message_queue')

    def callback(ch, method, properties, body):
        print(f"받은 메시지: {body.decode()}")

    channel.basic_consume(queue='message_queue', on_message_callback=callback, auto_ack=True)

    print('메시지를 기다리는 중입니다. 종료하려면 CTRL+C를 누르세요.')
    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("종료되었습니다.")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)