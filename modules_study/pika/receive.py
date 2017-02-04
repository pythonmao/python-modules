import pika 

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.exchange_declare(exchange='test_fanout1', type='fanout')
channel.queue_bind(exchange='test_fanout1', queue='hello')

def callback(ch, method, properites, boby):
    print 'revcicve hello world!: %s' % boby

channel.basic_consume(callback, queue='hello', no_ack=True)
#channel.basic_publish(exchange='', routeing_key='hello', boby='hello world')
#print '[x] send "hello world!"'
# while 1:
#     connection.process_data_events()
channel.start_consuming()
