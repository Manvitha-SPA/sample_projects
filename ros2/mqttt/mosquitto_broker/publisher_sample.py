
import paho.mqtt.publish as publish

# Replace these values with your MQTT broker configuration
broker_address = "localhost"
topic = "sample"
message = "Hello, MQTT!"

try:
    publish.single(topic, message, hostname=broker_address, port=1883, client_id="MQTT",
                   auth={'username': 'mosquitto_broker', 'password': 'mbroker'}, qos=0, retain=False)
    print("Message published successfully")
except Exception as e:
    print(f"Error publishing message: {str(e)}")