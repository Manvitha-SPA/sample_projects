from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'mqtt_to_ros'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='manvitha',
    maintainer_email='manvitha@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mqtt_subscriber_node = mqtt_to_ros.sub:main',
            'mqtt_bridge_node = mqtt_to_ros.bridge_node:main',
        ],
    },
)

