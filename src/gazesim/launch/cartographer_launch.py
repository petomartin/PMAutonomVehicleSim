from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='cartographer_ros',
            executable='cartographer_occupancy_grid_node',
            name='cartographer_node',
            output='screen',
            parameters=[
                {'use_sim_time': True},
                {'configuration_directory': '/home/petomartin/ros2_ws/src/gazesim/config'},
                {'configuration_basename': 'backpack_2d.lua'}
            ]
        ),
        Node(
            package='cartographer_ros',
            executable='cartographer_occupancy_grid_node',
            name='occupancy_grid_node',
            output='screen',
            parameters=[
                {'use_sim_time': True}
            ]
        )
    ])
