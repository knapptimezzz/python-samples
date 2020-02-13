#!/usr/bin/env python3

# Libraries
import os
import time
import pika
import random
import sys
sys.path.append('../protobuf_code')
import ot_data_pb2
import hiota_message_pb2
import common_pb2
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf import message

# Configurables
messages_per_second = int(os.environ['DP_MESSAGE_HZ'])  # Best to pick between 1 - 100
binding_key = os.environ['DP_BINDING_KEY']              # Channel data will be posted to
trace_id = os.environ['DP_TRACE_ID']                    # ID used for routing message
exchange_name = os.environ['DP_EXCHANGE_NAME']          # The name of the exchange
rabbit_user_name = os.environ['AMQP_USERNAME']          # The username for access to AMQP
rabbit_password = os.environ['AMQP_PASSWORD']           # The password for access to AMQP
amqp_broker = os.environ['AMQP_HOSTNAME']               # The address of the AMQP broker
amqp_port = int(os.environ['AMQP_PORT'])                # The port number of the AMQP broker (this will remain the same for all lumada instances)
isDuplicated = False                                    # Tell the generator to generate duplicate data
previous_value = 0
seed_value = None

# See the random number generator
random.seed(seed_value)

# Connection Setup Information
credentials = pika.PlainCredentials(username=rabbit_user_name, password=rabbit_password)
connection_params = pika.ConnectionParameters(host=amqp_broker, port=amqp_port, credentials=credentials, connection_attempts=5, socket_timeout=5, ssl=True)

# Infinite loop
try:

    # Try the connection
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # Infinite loop
    while True:
        
        # Generate additional information about the data point (if needed)
        raw_data = {}
        value = common_pb2.Value()
        value.string = "San Francisco, CA, USA"
        raw_data["City"] = value

        # Generate (or fetch) current time. MUST BE A PROTOBUF TIME!
        current_time = Timestamp()
        current_time.GetCurrentTime()

        # Generate the actual data for the generic datapoint
        value = common_pb2.Value()
        # Handle duplicate data for the deduplication demo
        if isDuplicated and random.randint(0, 2) == 1:
            value.sint64 = previous_value
        else:
            value.sint64 = random.randint(0, 100)
            previous_value = value.sint64

        # Generate a generic data point
        generic_data_point = ot_data_pb2.GenericDataPoint(data_descriptor_id="Test Data", value=value, properties=raw_data)

        # Create the OTData object with the generic data point
        ot_dat = ot_data_pb2.OTData(data_point=generic_data_point)

        # Generate the payload
        pay_load = (hiota_message_pb2.HiotaMessage(id="1", created=current_time, trace_id=[trace_id], ot_data=ot_dat))

        # Debug
        print("PAYLOAD FOR CDM MESSAGE: \n" + str(pay_load))
        
        # Serialize the payload (must use Protobuf serialization)
        pay_load = pay_load.SerializeToString()

        # Send the message to the broker
        channel.basic_publish(exchange=exchange_name, routing_key=binding_key, body=pay_load)

        # Debug
        time.sleep(1.0/messages_per_second)

except KeyboardInterrupt:
    connection.close()
    print("Script Exited")

except pika.exceptions.ConnectionClosed:
    print("Unable to connect to AMQP broker. The connection timed out.")
    print("Message Rate: " + str(messages_per_second))
    print("Binding Key: " + binding_key)
    print("Trace ID: " + trace_id)
    print("Exchange Name: " + exchange_name)
    print("Rabbit User Name: " + rabbit_user_name)
    print("Rabbit Password: " + rabbit_password)
    print("Broker IP: " + amqp_broker)
    print("Broker Port: " + str(amqp_port))
