#!/usr/bin/env python3

# Libraries
import os
import pika
import alert_data_pb2
import hiota_message_pb2
import common_pb2
from google.protobuf.timestamp_pb2 import Timestamp

# Configurables
binding_key = os.environ['ALERT_BINDING_KEY']           # Channel data will be posted to
trace_id = os.environ['ALERT_TRACE_ID']                 # ID used for routing message
exchange_name = os.environ['EXCHANGE_NAME']             # The name of the exchange
rabbit_user_name = os.environ['AMQP_USERNAME']          # The username for access to AMQP
rabbit_password = os.environ['AMQP_PASSWORD']           # The password for access to AMQP
amqp_broker = os.environ['AMQP_HOSTNAME']               # The address of the AMQP broker
amqp_port = int(os.environ['AMQP_PORT'])                # The port number of the AMQP broker (this will remain the same
                                                        # for all lumada instances)
isDuplicated = True                                     # Tell the generator to generate duplicate data
previous_value = 0
seed_value = None

def hiota_alert_message_pop(alert_msg, severity=2, alert_data=None):
    # Connection Setup Information
    credentials = pika.PlainCredentials(username=rabbit_user_name, password=rabbit_password)
    connection_params = pika.ConnectionParameters(host=amqp_broker, port=amqp_port, credentials=credentials,
                                                  connection_attempts=5, socket_timeout=5, ssl=True)
    try:
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()

        # Generate additional information about the data point (if needed)
        raw_data = {}
        value = common_pb2.Value()
        value.string = "San Francisco, CA, USA"
        raw_data["City"] = value

        # Generate (or fetch) current time. MUST BE A PROTOBUF TIME!
        current_time = Timestamp()
        current_time.FromMicroseconds(int(alert_data["timestamp"]))

        # Create the alert message
        alert_dat = alert_data_pb2.AlertData(name="Alert Test", description=alert_msg,
                                             severity=severity,    # ALERT_SEVERITY_WARNING
                                             type=1                # ALERT_TYPE_CUSTOM
                                             )
        asset_str = "data-pump"
        asset_name = "Hiota_Alert_Tester"
        asset_info = hiota_message_pb2.AssetInfo(urn=alert_data["assetUrn"], name=asset_name)

        # device_info = hiota_message_pb2.DeviceInfo(urn=alert_data["deviceUrn"], name="")

        # Generate the payload
        pay_load = (hiota_message_pb2.HiotaMessage(id="1", created=current_time, trace_id=[trace_id],
                                                   asset_info=asset_info, alert_data=alert_dat))

        # Debug
        print("PAYLOAD FOR CDM MESSAGE: \n" + str(pay_load))

        # Serialize the payload (must use Protobuf serialization)
        pay_load = pay_load.SerializeToString()

        # Send the message to the broker
        channel.basic_publish(exchange=exchange_name, routing_key=binding_key, body=pay_load)

    except KeyboardInterrupt:
        connection.close()
        print("Script Exited")

    except pika.exceptions.ConnectionClosed:
        print("Unable to connect to AMQP broker. The connection timed out.")
        print("Binding Key: " + binding_key)
        print("Trace ID: " + trace_id)
        print("Exchange Name: " + exchange_name)
        print("Rabbit User Name: " + rabbit_user_name)
        print("Rabbit Password: " + rabbit_password)
        print("Broker IP: " + amqp_broker)
        print("Broker Port: " + str(amqp_port))