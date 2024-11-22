from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '/home/petomartin/labirintus2SLAM.world',
                 '-s', 'libgazebo_ros_factory.so'],
            output='screen'),

        Node(
            package='gazesim',
            executable='status_logger_node',
            name='status_logger',
            output='screen',
            #parameters=[{'simulation_running': True}] 
            ),
        
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': '/home/petomartin/ros2_ws/src/gazesim/urdf/prius.urdf'}]
        ),
        
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='spawn_prius',
            output='screen',
            parameters=[{'robot_name': 'prius', 'x': 0.0, 'y': 0.0, 'z': 0.0}],
            arguments=[
                '-entity', 'prius',
                '-file', '/home/petomartin/ros2_ws/src/gazesim/urdf/prius.urdf',  #/home/petomartin/.gazebo/models/prius_hybrid_sensors/model.sdf
                '-x', '0', '-y', '0', '-z', '0',
                '-Y', '1.5708'  # 90 fokos balra fordulás (yaw) 1.5708
            ],
        ),
    ])
