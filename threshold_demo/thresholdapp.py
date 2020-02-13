#!/usr/bin/env python3

# Libraries
import time
import pika
import ot_data_pb2
import hiota_message_pb2
import common_pb2
import os
import json
from datetime import datetime
from influxdb import InfluxDBClient
import urllib3
import hiota_alert

# Disable the warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configurables
rabbit_username = str(os.environ['AMQP_USERNAME'])
rabbit_password = str(os.environ['AMQP_PASSWORD'])
amqp_broker = str(os.environ['AMQP_HOSTNAME'])
amqp_port = int(os.environ['AMQP_PORT'])
debug = int(os.environ['AMQP_DEBUG_BOOLEAN'])
threshold_value = float(os.environ["THRESHOLD_VALUE"])
trace_id = str(os.environ['TRACE_ID'])
input_binding_key = str(os.environ['INPUT_BINDING_KEY'])
input_queue = str(os.environ['INPUT_QUEUE'])
output_binding_key = str(os.environ['OUTPUT_BINDING_KEY'])
exchange_name = str(os.environ["EXCHANGE_NAME"])
discard_alert_value = int(os.environ["DISCARD_ALERT_VALUE"])
save_to_influx = int(os.environ["STORE_ALERTS"])
influx_hostname = str(os.environ["DEMO_INFLUX_HOSTNAME"])
influx_port = int(os.environ["DEMO_INFLUX_PORT"])
influx_username = str(os.environ["INFLUX_USERNAME"])
influx_password = str(os.environ["INFLUX_PASSWORD"])
data_source = str(os.environ["SOURCE"])
data_to_process = str(os.environ["DATA_MODEL"])
database = str(os.environ["DATA_BASE_NAME"])
alerts_table = str(os.environ["ALERTS_TABLE_NAME"])
severity_level = int(os.environ["ALERT_SEVERITY"])

# Create a handler to process each message as it comes in
def processmessage(ch, method, properties, body):

    if debug:
        print("Processing a message.")

    # Recieve the message and parse out the data
    message = hiota_message_pb2.HiotaMessage()
    message.ParseFromString(body)
    pay_load = (hiota_message_pb2.HiotaMessage(id=message.id, created=message.created, trace_id=[trace_id], ot_data=message.ot_data))

    if debug:
        print(pay_load)

    # Handle roll, pitch, yaw data from iPhone
    if data_source == "iphone" and data_to_process == "json":
        # Get the value
        json_data = json.loads(message.ot_data.data_point.value.binary)

        try:
            yaw = json_data["yaw"]
            roll = json_data["roll"]
            pitch = json_data["pitch"]

            # Debug
            if debug:
                print(json_data)

            # If the user wants to discard the alerted value
            if abs(yaw) > threshold_value or abs(roll) > threshold_value or abs(pitch) > threshold_value:
                # Log the value out to the terminal
                alert_msg = "ALERT!! The absolute value is over " + str(threshold_value) + \
                            ". Current values are (yaw: " + str(yaw) + ", roll: " + str(roll) + ", pitch: " + \
                            str(pitch) + ")"
                print(alert_msg)
                hiota_alert.hiota_alert_message_pop(alert_msg, severity=severity_level)
                # If the user wants to save the data to an influx table
                if save_to_influx:
                    # Create local time variable
                    local_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
                    # Switch to Database
                    client.switch_database(database)
                    # Influx data
                    influx_data = [
                        {
                            "measurement": alerts_table,
                            "tags": {},
                            "time": local_time,
                            "fields": {
                                "yaw": yaw,
                                "roll": roll,
                                "pitch": pitch
                            }
                        }
                    ]
                    # Write the data to influx
                    client.write_points(influx_data)
        except KeyError:
            print("Data does not include 'yaw,' 'pitch,' and 'roll.' Your configuration is set up to read iPhone-JSON data for yaw, pitch, and roll.")

    # Handle data coming from the data pump in xhiota format
    elif data_source == "datapump":
        # Get the value
        value = message.ot_data.data_point.value.sint64

        # Debug
        if debug:
            print(pay_load)

        # If the user wants to discard the alerted value
        if value > threshold_value:
            # Log the value out to the terminal
            alert_msg = "ALERT!! The value is over " + str(threshold_value) + ". Current value is " + str(value)
            print(alert_msg)
            hiota_alert.hiota_alert_message_pop(alert_msg, severity=severity_level)
            if not discard_alert_value:
                # Serialize the payload (must use Protobuf serialization)
                pay_load = pay_load.SerializeToString()
                # Publish the message back to the Lumada system so it can be sent to the database
                channel.basic_publish(exchange=exchange_name, routing_key=output_binding_key, body=pay_load)
        else:
            # Serialize the payload (must use Protobuf serialization)
            pay_load = pay_load.SerializeToString()
            # Publish the message back to the Lumada system so it can be sent to the database
            channel.basic_publish(exchange=exchange_name, routing_key=output_binding_key, body=pay_load)

# Connect to RabbitMQ AMQP instance
credentials = pika.PlainCredentials(username=rabbit_username, password=rabbit_password)
connection_params = pika.ConnectionParameters(host=amqp_broker, port=amqp_port, credentials=credentials, connection_attempts=5, socket_timeout=5, ssl=True)

# Create a client to connect with Influxdb
client = InfluxDBClient(host=influx_hostname, port=influx_port, username=influx_username, password=influx_password, ssl=True, verify_ssl=False)

# Infinite loop
try:

    if debug:
        print("Threshold app starting.")

    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    if debug:
        print("Pika connections set.")

    # Create a queue and bind to it
    channel.queue_declare(queue=input_queue)
    channel.queue_bind(exchange=exchange_name, queue=input_queue, routing_key=input_binding_key)

    if debug:
        print("Bound to pika queue.")

    # Create a callback method to handle incoming messages
    channel.basic_consume(processmessage, queue=input_queue, no_ack=True)
    channel.start_consuming()

except KeyboardInterrupt:
    connection.close()
    print("Script Exited")

except pika.exceptions.ConnectionClosed:
    print("Unable to connect to AMQP broker. The connection timed out.")
    print("Input Binding Key: " + input_binding_key)
    print("Input Queue: " + input_queue)
    print("Output Binding Key: " + output_binding_key)
    print("Trace ID: " + trace_id)
    print("Exchange Name: " + exchange_name)
    print("Rabbit User Name: " + rabbit_username)
    print("Rabbit Password: " + rabbit_password)
    print("Broker IP: " + amqp_broker)
    print("Broker Port: " + str(amqp_port))
    print("Debug Flag: " + str(debug))
    print("Threshold Value: " + str(threshold_value))