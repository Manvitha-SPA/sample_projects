import paho.mqtt.client as mqtt
import rclpy
from std_msgs.msg import String
import yaml

def load_mqtt_config(config_file):
    import os
    absolute_path = os.path.abspath(config_file)
    
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config['broker']

class ROS2Node:
    def __init__(self, topic):
        self.node = rclpy.create_node('mqtt_bridge_node')
        self.publisher = self.node.create_publisher(String, topic, 10)

    def publish_message(self, message, result_code):
        ros2_message = String()
        ros2_message.data = f"{message}, Result Code: {result_code}"
        self.publisher.publish(ros2_message)

    def spin(self):
        rclpy.spin(self.node)

    def destroy(self):
        self.node.destroy_node()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    message = msg.payload.decode("utf-8")
    print("Received message: {}".format(message))

    # Process the message, get result_code
    result_code = len(message)

    # Publish to ROS2 topic
    ros2_node.publish_message(message, result_code)

def graceful_shutdown(signum, frame):
    print("Shutting down gracefully...")
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    
    try:
        ros2_node.destroy()
    except Exception as e:
        print(f"Error during ROS2 node destruction: {e}")

    rclpy.shutdown()

def main():
    global mqtt_client, ros2_node, MQTT_TOPIC

    rclpy.init()

    # Load MQTT config from YAML file
    mqtt_config = load_mqtt_config('/home/manvitha/ros2_ws/src/mqtt_to_ros/config/mqtt_ros_bridge.yaml')

    # Constants
    MQTT_BROKER = mqtt_config['host']
    MQTT_PORT = mqtt_config['port']
    MQTT_USERNAME = mqtt_config['username']
    MQTT_PASSWORD = mqtt_config['password']
    MQTT_TOPIC = "pingpong/ros"
    ROS2_TOPIC = "/pong/ros"

    # Set up MQTT client with username and password
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(username=MQTT_USERNAME, password=MQTT_PASSWORD)
    mqtt_client.on_connect = on_connect
    mqtt_client.on_message = on_message

    # Connect to MQTT broker
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)

    # Set up ROS2 node
    ros2_node = ROS2Node(ROS2_TOPIC)

    # Start the MQTT loop
    mqtt_client.loop_start()

    # Register signal handler for graceful shutdown
    import signal
    signal.signal(signal.SIGINT, graceful_shutdown)

    # Keep the script running to receive messages
    try:
        while True:
            mqtt_client.loop(timeout=1.0, max_packets=1)
            ros2_node.spin()
    except KeyboardInterrupt:
        pass
    finally:
        graceful_shutdown(None, None)

if __name__ == '__main__':
    main()
