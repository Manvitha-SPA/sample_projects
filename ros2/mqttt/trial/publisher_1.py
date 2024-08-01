import paho.mqtt.publish as publish

def on_publish(client, userdata, mid):
    print("Message Published")

host = "54.226.64.227"  # Replace with your Mosquitto broker IP or hostname
port = 1883  # Replace with the port number if different from the default (1883)
topic = "sample/topic01"  # Replace with the desired topic
username = "srinivas18"  # Replace with your MQTT broker username
password = "mosquitto"  # Replace with your MQTT broker password

# Define the message to be published
message = "Good Evening!"

# Set the MQTT connection parameters
auth = {'username': username, 'password': password}
tls_params = None  # Set TLS parameters if using a secure connection (e.g., {'ca_certs': 'path/to/ca.crt'})

# Publish the message
publish.single(topic, payload=message, qos=1, hostname=host, port=port, auth=auth, tls=tls_params)

print("Publishing message...")