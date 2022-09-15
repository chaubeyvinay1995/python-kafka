from json import dumps
from kafka import KafkaProducer
from config import Config

producer = KafkaProducer(bootstrap_servers=[Config.KAFKA_SERVER_ADDRESS],
                         value_serializer=lambda x: dumps(x).encode('utf-8'))
for e in range(1000):
    data = {'number': e}
    # name of the topic here in my case its is kafka-python
    producer.send(topic='kafka-python', value=data)
    # below line will send message in synchronous way, if we remove this line then it will send in asynchronous way
    producer.flush()
