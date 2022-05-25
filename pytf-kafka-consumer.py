from kafka import KafkaConsumer
import json


def receive_to_kafka():
    consumer = KafkaConsumer('terraform_resource_info',# group_id="my_group",
                             bootstrap_servers=['cnshc-dbtest-t01001:9092'],
                             auto_offset_reset='latest', # earliest or latest
                             value_deserializer=json.loads)
    for msg in consumer:
        print(msg)
        # recv = "%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value)
        # print(recv)

    consumer.close()


if __name__ == "__main__":
    receive_to_kafka()

