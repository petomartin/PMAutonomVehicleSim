from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Get the path to your package
    pkg_my_gazebo_package = get_package_share_directory('my_gazebo_package')
    
    # Path to the world file
    world_path = PathJoinSubstitution([pkg_my_gazebo_package, 'world', 'my_world.world'])
    
    # Path to the Gazebo launch file (update with the actual path if needed)
    gz_launch_path = PathJoinSubstitution([get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py'])

    return LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value=str(world_path),
            description='World file to load into Gazebo'
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(gz_launch_path),
            launch_arguments={
                'world': LaunchConfiguration('world'),
                'paused': 'false',  # Set to true if you want Gazebo to start paused
                'gui': 'true'  # Set to false if you don't want the GUI
            }.items(),
        ),
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            arguments=[],
            remappings=[],
            output='screen'
        ),
    ])
