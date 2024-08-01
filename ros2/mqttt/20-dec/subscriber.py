import paho.mqtt.client as mqtt
import time
import subprocess
 
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe("test/topic")
 
def on_message(client, userdata, msg):
    command = ["colcon build","source ~/.bashrc"]
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
    decoded_payload = msg.payload.decode()
    command.append(decoded_payload)
    for i in command:
 
 
    # Run the command in a shell
        result = subprocess.run(['bash', '-c', f'cd /home/manvitha/ros2_ws && {command}'],
                            check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True , shell= True)
 
    # Print the output
    print("Output:", result.stdout)
 
    # Disconnect from the broker after receiving a single message
    client.disconnect()
 
# Replace with your MQTT broker information
mqtt_broker_address = "54.227.224.199"
mqtt_broker_port = 1883
mqtt_username = "srinivas18"  # Replace with your MQTT username
mqtt_password = "mosquitto"  # Replace with your MQTT password
 
client = mqtt.Client()
client.username_pw_set(username=mqtt_username, password=mqtt_password)
client.on_connect = on_connect
client.on_message = on_message
 
client.connect(mqtt_broker_address, mqtt_broker_port, 60)
 
# Start the loop in a separate thread
client.loop_start()
 
# Wait for 30 seconds
time.sleep(30)
 
# Stop the loop and disconnect from the broker
client.loop_stop()
client.disconnect()