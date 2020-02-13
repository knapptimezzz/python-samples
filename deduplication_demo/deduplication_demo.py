#!/usr/bin/env python3

# Libraries
import time
import pika
import ot_data_pb2
import hiota_message_pb2
import common_pb2
import os
import json

# Configurables    
rabbit_username = str(os.environ['AMQP_USERNAME'])     
rabbit_password = str(os.environ['AMQP_PASSWORD'])      
amqp_broker = str(os.environ['AMQP_HOSTNAME'])        
amqp_port = int(os.environ['AMQP_PORT']) 
debug = int(os.environ['DEBUG_BOOLEAN'])
input_binding_key = str(os.environ['INPUT_BINDING_KEY'])
input_queue = str(os.environ['INPUT_QUEUE'])
output_binding_key = str(os.environ['OUTPUT_BINDING_KEY'])
exchange_name = str(os.environ["EXCHANGE_NAME"])
trace_id = str(os.environ["TRACE_ID"])
previous_value = -1

# Create a handler to process each message as it comes in
def processmessage(ch, method, properties, body):

    global previous_value

    # Recieve the message and parse out the data
    message = hiota_message_pb2.HiotaMessage()
    message.ParseFromString(body)
    pay_load = (hiota_message_pb2.HiotaMessage(id=message.id, created=message.created, trace_id=[trace_id], ot_data=message.ot_data))
    
    # Get the value
    value = int(message.ot_data.data_point.value.sint64)

    # Debug
    if debug:
        print(pay_load)

    if value == previous_value:
        print ("Duplicate date removed. Duplicate value is " + str(value))
    else:
        # Serialize the payload (must use Protobuf serialization)
        pay_load = pay_load.SerializeToString()

        # Publish the message back to the Lumada system so it can be sent to the database
        channel.basic_publish(exchange=exchange_name, routing_key=output_binding_key, body=pay_load)
    
    # Set the previous value
    previous_value = value


# Connect to RabbitMQ AMQP instance
credentials = pika.PlainCredentials(username=rabbit_username, password=rabbit_password)
connection_params = pika.ConnectionParameters(host=amqp_broker, port=amqp_port, credentials=credentials, connection_attempts=5, socket_timeout=5, ssl=True)

# Infinite loop
try:

    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # Create a queue and bind to it
    channel.queue_declare(queue=input_queue)
    channel.queue_bind(exchange=exchange_name, queue=input_queue, routing_key=input_binding_key)

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
    print("Exchange Name: " + exchange_name)
    print("Rabbit User Name: " + rabbit_username)
    print("Rabbit Password: " + rabbit_password)
    print("Broker IP: " + amqp_broker)
    print("Broker Port: " + str(amqp_port))
    print("Debug Flag: " + str(debug))