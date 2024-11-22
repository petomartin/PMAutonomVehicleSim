from setuptools import find_packages, setup
from glob import glob  # Add this line to import glob
package_name = 'gazesim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/gazesim_launch.py']),  # Launch fájl helyes elérési útja
       # ('share/' + package_name + '/launch', ['launch/cartographer_launch.py']),
       # ('share/' + package_name + '/config', glob('config/my_robot_cartographer.lua')),  # Minden config fájl
        ('share/' + package_name + '/launch', ['launch/display.launch.py']),
        ('share/' + package_name + '/launch', ['launch/vehicle_launch.py']),
      #  ('share/' + package_name + '/launch', ['launch/slam_world_launch.py']),
        ('share/' + package_name + '/launch', ['launch/online_async_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='petomartin',
    maintainer_email='peto.martin@icloud.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'status_logger_node = gazesim.status_logger_node:main',  # Node végrehajtási pont
            'sensor_handler_node = gazesim.sensor_handler_node:main',
            'teleop_node = gazesim.teleop_node:main',
            'tervezo = gazesim.tervezo:main',
        ],
    },
)
