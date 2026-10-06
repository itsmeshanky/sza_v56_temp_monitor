from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='temp_monitor',
            executable='temp_generator',
            name='temp_generator',
            output='screen'
        ),
        Node(
            package='temp_monitor',
            executable='temp_monitor',
            name='temp_monitor',
            output='screen'
        )
    ])