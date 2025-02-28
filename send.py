import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='message_queue')

while True:  # 메시지를 계속 입력받기 위한 루프
    message = input("전송할 메시지를 입력하세요 (종료하려면 'exit' 입력): ")
    if message.lower() == 'exit':  # 'exit' 입력 시 종료
        break
    channel.basic_publish(exchange='', routing_key='message_queue', body=message)
    print("메시지가 전송되었습니다.")

connection.close()