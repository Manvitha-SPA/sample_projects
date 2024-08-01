import paho.mqtt.client as mqttclient
import time

def on_connect(client, userdata, flags, rc):
    print('Hello here')
    if rc == 0:
        print("Client is connected")
        client.connected_flag = True
    else:
        print("Client is not connected")

connected = False
broker_address = "8763b78320de427faee93143f9d4a242.s2.eu.hivemq.cloud"
port = 8883
user = "manvitha"
print('hii')
password = "Spaplc1!"
print('dfghjkl')

client = mqttclient.Client("MQTT")
client.username_pw_set(user, password=password)
print('hERe1')
client.connected_flag = False  # Add the connected_flag attribute
client.on_connect = on_connect
print('here2')
client.connect(broker_address, port=port)
print('here3')
client.loop_start()

while not client.connected_flag:  # Wait for the connection to be established
    time.sleep(1)

print('here4')
result = client.publish("mqtt/firstcode", "Hello MQTT")
print(f"Publish result: {result}")
time.sleep(1)
client.loop_stop()

 
'''def on_message (client, userdata, message):
    print ("message received " ,str (message.payload.decode ("utf-8")))
    print ("message topic=", str(message.topic))
Messagerecieved=False

 
 
connected=False
#Messagerecieved=False
broker_address="8763b78320de427faee93143f9d4a242.s2.eu.hivemq.cloud"
port=8883
user="manvitha"
password="Spaplc1!"
client=mqttclient.Client ("MQTT")
client.username_pw_set (user, password=password)
client.on_connect=on_connect
client.connect (broker_address, port=port)
client.loop_start()
client.subscribe ("mqtt/secondcode")
while connected!=True:
    time.sleep (0.2)
client.publish()
client.loop_stop()

'''



