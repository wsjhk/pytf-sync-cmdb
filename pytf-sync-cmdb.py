from libterraform import TerraformCommand
from kafka import KafkaProducer
import json, os, time


def datasource_apply():
    cli = TerraformCommand()
    tfstate_path = 'import_resource_list.tfstate'
    if os.path.exists(tfstate_path):
        os.remove(tfstate_path)

    r = cli.apply(state_out="import_resource_list.tfstate")
    return r

def import_resource():
    cli = TerraformCommand()

    with open('import_resource_list.tfstate', 'r', encoding='utf8') as tf:
        json_data = json.load(tf)

    id_list = json_data['outputs']['slb_ids']['value']
    id_list += json_data['resources'][0]['instances'][0]['attributes']['ids']

    for id in id_list:
        print(id)
        if "lb-" in id:
            res = cli.import_resource(addr="alicloud_slb.slb_instance", id=id)
        elif 'i-' in id:
            res = cli.import_resource(addr="alicloud_instance.ecs_instance", id=id)
        else:
            res = None
        print(res)

def on_send_success(record_metadata):
    print(record_metadata.topic, record_metadata.partition, record_metadata.offset)


def on_send_error(exception):
    pass


def send_to_kafka(instance):
    producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'),
                             bootstrap_servers=['cnshc-dbtest-t01001:9092'])
    try:
        future = producer.send('terraform_resource_info', instance).add_callback(on_send_success).add_callback(on_send_error)
        result = future.get(timeout=2)
        print(result)
    except Exception as e:
        print(str(e))
    finally:
        producer.close()


def resourceinfo_cover_to_msg():
    json_data = datasource_apply().value[4]
    # print(json.dumps(json_data, indent=2))
    resource_list = ["slb_info_xmotors_ai", "slb_info_139", "slb_info_179", "ecs_info_xmotors_ai", "ecs_info_139", "ecs_info_179",
                     "ecs_info_aws", "mongodb_info_xmotors_ai", "mongodb_info_139", "mongodb_info_179", "rds_info_xmotors_ai",
                     "rds_info_139", "rds_info_179", "nas_info_xmotors_ai", "nas_info_139", "nas_info_179", "oss_info_xmotors_ai",
                     "oss_info_139", "oss_info_179"]
    for instance_type in resource_list:
        instance_list = json_data["outputs"][instance_type]["value"]
        # print(type(instance_list))
        if instance_list and type(instance_list) != dict:
            for instance in instance_list:
                instance["tf_resource_type"] = instance_type
                # print(instance)
                send_to_kafka(instance)
        elif type(instance_list) == dict or type(instance_list) == str:
            print("This resource type: %s is dict or string,not list,Please to check!" % (instance_type))
        else:
            print("This resource type: %s is NULL.No msg to send kafka!" % (instance_type))


if __name__ == "__main__":
    start_time = time.strftime('%Y-%m-%d %H:%M:%S')

    resourceinfo_cover_to_msg()

    end_time = time.strftime('%Y-%m-%d %H:%M:%S')

    print("Start time ~ End time: %s ~ %s" % (start_time, end_time))

