from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='rad121_monitor',
            executable='rad_action_node',
            name='rad_action_node',
            output='screen'
        )
    ])

