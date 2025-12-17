# turtle_color.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    # 파라미터를 주입한 Turtlesim 노드
    # 1. Turtlesim 시뮬레이터
    turtlesim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='norm',
        namespace='room1',
        output='screen'
    )

    yellow_turtlesim = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='yellow',
        namespace='room2',
        output='screen',
        parameters=[
            {'background_r': 255}, # Red
            {'background_g': 255},   # Green
            {'background_b': 0}    # Blue
        ]
    )


    my_circle_node = Node(
        package='my_turtle_pkg',
        executable='circle_node',
        name='my_driver',
        output='screen',
        remappings=[('/cmd_vel', '/room2/turtle1/cmd_vel')]
    )

    return LaunchDescription([
        turtlesim_node,
        yellow_turtlesim,
        my_circle_node
    ])