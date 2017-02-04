import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
print type(channel)
channel.queue_declare(queue='hello')
channel.exchange_declare(exchange='test_fanout', type='fanout')
# channel.basic_publish(exchange='', routing_key='hello', body='hello world!')
channel.basic_publish(exchange='test_fanout', routing_key='', body='hello world!')
print '[x] send "hello world!"'
connection.close()
