import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, Command
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import launch_ros
import os

def generate_launch_description():
    pkg_share = os.path.join(os.getenv('HOME'), 'ros2_ws/src/gazesim')
   # default_model_path = os.path.join(pkg_share, 'urdf/my_robot.urdf')
    default_model_path = os.path.join(pkg_share, 'urdf', 'prius.urdf')
    

    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{'robot_description': Command(['xacro ', LaunchConfiguration('model')])}]
    )
    
    joint_state_publisher_node = launch_ros.actions.Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        parameters=[{'use_sim_time': True}]
    )

    spawn_entity = launch_ros.actions.Node(
    package='gazebo_ros',
    executable='spawn_entity.py',
    arguments=['-entity', 'my_first_robot', '-topic', 'robot_description'],
    output='screen'
    )
    
    ##spawn_entity = launch_ros.actions.Node(
      ##  package='gazebo_ros',
      ##  executable='spawn_entity.py',
      ##  arguments=['-entity', 'my_first_robot', '-topic', 'robot_description'],
      ##  output='screen'
    ##)

     
    
    return launch.LaunchDescription([
        launch.actions.DeclareLaunchArgument(name='model', default_value=default_model_path,
                                            description='Absolute path to robot urdf file'),
        launch.actions.ExecuteProcess(cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'], output='screen'),
        joint_state_publisher_node,
        robot_state_publisher_node,
        spawn_entity,
    ])