# waffle_pi.launch.py
import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    
    # FindPackageShare : 런치파일 관련 내용이 포함된 share 폴더에서 특정 패키지 경로 찾기 
    pkg_gazebo_ros = FindPackageShare(package='turtlebot3_gazebo').find('turtlebot3_gazebo')

		# 가제보 패키지를 찾았으니, 그 안에 있는 런치파일을 포함해서 이 런치파일을 실행하겠다
    start_gazebo_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'turtlebot3_world.launch.py')
        )
    )

    my_circle_node = Node(
        package='my_turtle_pkg',
        executable='circle_node',
        name='waffle_driver',
        output='screen'
    )

    return LaunchDescription([
        start_gazebo_cmd,
        my_circle_node
    ])