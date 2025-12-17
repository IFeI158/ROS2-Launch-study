# launch/arg_test.launch.py
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    # 1. Argument 선언 (받을 준비)
    # 실행 시 'target_speed'라는 값을 안 주면 기본값 '2.0'을 쓴다.
    speed_arg = DeclareLaunchArgument(
        'target_speed', 
        default_value='2.0',
        description='Speed of the robot'
    )

    # 2. Configuration으로 값 잡기 (받은 값 활용)
    speed_config = LaunchConfiguration('target_speed')

    node = Node(
        package='my_turtle_pkg',
        executable='param_node',
        output='screen',
        parameters=[
            # 런치 Argument로 받은 값을 -> 노드의 Parameter로 토스!
            {'my_speed': speed_config} 
        ]
    )

    return LaunchDescription([
        speed_arg,
        node
    ])