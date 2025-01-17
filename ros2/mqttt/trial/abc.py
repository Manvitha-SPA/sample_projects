import paho.mqtt.client as mqtt

# Callbacks
def on_connect(client, userdata, flags, rc):
    print("Connected with Code: " + str(rc))
    # Subscribe Topic after connecting
    client.subscribe("topic1")
    
    

def on_message(client, userdata, msg):
    print(f"Received message on topic: {msg.topic}")
    print(f"Message payload: {msg.payload.decode('utf-8')}")

client = mqtt.Client("MQTT")
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect("localhost", 1883, 60)
client.username_pw_set("mosquitto_broker", "mbroker")

# Enter the network loop
client.loop_forever() 
'''
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import paho.mqtt.client as mqtt
import yaml

class MqttRosBridge(Node):
    def __init__(self, config_file):
        super().__init__('mqtt_ros_bridge')

        self.ros_publisher = self.create_publisher(String, '/pong/ros', 10)
        self.mqtt_config = self.load_mqtt_config(config_file)

        self.mqtt_client = mqtt.Client()
        self.mqtt_client.on_connect = self.on_connect
        self.mqtt_client.on_disconnect = self.on_disconnect
        self.mqtt_client.on_message = self.on_message

        try:
            mqtt_broker_address = self.mqtt_config['broker']['host']
            mqtt_broker_port = self.mqtt_config['broker']['port']
            mqtt_topic = self.mqtt_config['bridge']['mqtt2ros'][0]['mqtt_topic']

            self.mqtt_client.connect(mqtt_broker_address, mqtt_broker_port, 60)
            self.mqtt_client.subscribe(mqtt_topic)
        except Exception as e:
            self.get_logger().error(f"Error connecting to MQTT broker: {e}")

    def on_connect(self, client, userdata, flags, rc):
        self.get_logger().info("Connected to MQTT broker with result code %s" % rc)

    def on_disconnect(self, client, userdata, rc):
        self.get_logger().info("Disconnected from MQTT broker with result code %s" % rc)

    def on_message(self, client, userdata, msg):
        mqtt_payload = msg.payload.decode()
        ros_topic = self.mqtt_config['bridge']['mqtt2ros'][0]['ros_topic']

        ros_msg = String()
        ros_msg.data = mqtt_payload
        self.ros_publisher.publish(ros_msg)
        self.get_logger().info(f"Published to ROS: {ros_msg.data}")

    def load_mqtt_config(self, config_file):
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
        return config

def main(args=None):
    rclpy.init(args=args)
    node = MqttRosBridge('/home/manvitha/ros2_ws/src/mqtt_to_ros/config/mqtt_ros_bridge.yaml')  # Replace with the actual path
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

'''
