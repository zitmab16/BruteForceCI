import  threading
import queue
from pwdProducer import PWDProducer
from pwdConsumer import PWDConsumer

queue = queue.Queue(maxsize=10)
condition = threading.Condition()

producer = PWDProducer(queue,condition)

consumer = PWDConsumer(queue,condition)
consumer2= PWDConsumer(queue,condition)

producer.start()
consumer.start()
consumer2.start()

producer.join()
consumer.join()
consumer2.join()

