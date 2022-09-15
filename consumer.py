from json import loads
from kafka import KafkaConsumer
from config import Config

consumer = KafkaConsumer(
    Config.TOPIC_NAME,
    bootstrap_servers=[Config.KAFKA_SERVER_ADDRESS],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

for message in consumer:
    message = message.value
    print('{}'.format(message))