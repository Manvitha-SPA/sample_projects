from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
#from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mqtt_to_ros',
            executable='mqtt_bridge_node',  # Replace with the actual name of your bridge node executable
            name='mqtt_bridge_node',
            output='screen',
            parameters=[{'config_file': '/home/manvitha/ros2_ws/src/mqtt_to_ros/config/mqtt_ros_bridge.yaml'}],  # Replace
        ),
        Node(
            package='mqtt_to_ros',
            executable='mqtt_subscriber_node',  # Replace with the actual name of your subscriber node executable
            name='mqtt_subscriber_node',
            output='screen',
        ),
    ])


