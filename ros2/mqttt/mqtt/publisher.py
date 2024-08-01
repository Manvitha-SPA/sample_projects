import ssl
from paho import mqtt
import paho.mqtt.client as paho
import paho.mqtt.publish as publish

# create a set of 2 test messages that will be published at the same time
msgs = [{'topic': "paho/test/multiple", 'payload': "test 1"}, ("paho/test/multiple", "test 2", 0, False)]

# use TLS for secure connection with HiveMQ Cloud
sslSettings = ssl.SSLContext(mqtt.client.ssl.PROTOCOL_TLS)

# put in your cluster credentials and hostname
auth = {'username': "manvitha", 'password': "Spaplc1!"}
publish.multiple(msgs, hostname="8763b78320de427faee93143f9d4a242.s2.eu.hivemq.cloud", port=8883, auth=auth,tls=sslSettings, protocol=paho.MQTTv31)

