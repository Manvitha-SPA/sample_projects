#!/usr/bin/env python

import rclpy
from std_msgs.msg import String

def callback(msg):
    rclpy.logging.get_logger('mqtt_subscriber_node').info("Received from /pingpong/ros: {}".format(msg.data))

def main():
    rclpy.init()
    node = rclpy.create_node('mqtt_subscriber_node')
    subscription = node.create_subscription(String, '/pong/ros', callback, 10)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
