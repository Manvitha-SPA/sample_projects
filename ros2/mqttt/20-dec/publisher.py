import paho.mqtt.client as mqtt
 
# Define the MQTT broker address, port, username, and password
broker_address = "54.227.224.199"
port = 1883
username = "srinivas18"
password = "mosquitto"
 
# Define the topic to publish to
topic = "test/topic"
 
# Create an MQTT client
client = mqtt.Client()
 
# Set username and password
client.username_pw_set(username, password)
 
# Connect to the broker
client.connect(broker_address, port, keepalive=60)
 
# Publish a single message to the topic
message = "ros2 launch ros_to_mqtt mqqt_bridge.launch.py"
client.publish(topic, message)
print(f"Published: {message}")
 
# Disconnect from the broker
client.disconnect()