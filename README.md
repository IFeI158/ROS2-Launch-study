# ROS2 Launch 

파일명,주요 학습 내용
arg_test.launch.py,Launch Arguments 사용법 학습: DeclareLaunchArgument를 이용해 외부에서 값을 받아와 Launch 파일 내에서 사용하는 방법을 시연합니다.
param_test.launch.py,Node Parameters 설정 학습: Parameter 액션을 사용하거나 노드를 선언할 때 파라미터 값을 직접 설정하여 노드의 동작을 변경하는 방법을 시연합니다.
turtle_color.launch.py,"turtlesim 노드의 파라미터 설정 및 변경: turtlesim_node를 실행하고, 파라미터를 설정하여 시뮬레이터 배경색을 변경하는 방법을 보여줍니다."
turtle_sim.launch.py,간단한 노드 실행 및 Launch 파일 구조: turtlesim 시뮬레이터와 turtle_teleop 노드를 동시에 실행하는 기본적인 Launch 파일 구조를 보여줍니다.
twin_turtles.launch.py,"노드 이름 및 네임스페이스 재매핑: 동일한 노드 타입(turtlesim_node)의 인스턴스를 두 개 실행하고, 각기 다른 node_name과 namespace를 부여하여 충돌 없이 동작하도록 구성합니다."
waffle_pi.launch.py,(추정) 실제 로봇 환경 시뮬레이션 구성: turtlebot3_gazebo와 같은 실제 로봇(예: Waffle Pi) 시뮬레이션 환경을 구동하기 위한 복합적인 노드 그룹 및 설정 예시입니다.
yaml_load.launch.py,YAML 파일로부터 파라미터 로드: 외부 .yaml 파일에 정의된 파라미터들을 LaunchConfiguration과 함께 사용하여 노드에 일괄적으로 적용하는 방법을 시연합니다.
