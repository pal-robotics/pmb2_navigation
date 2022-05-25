# Copyright (c) 2022 PAL Robotics S.L.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration, PythonExpression
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch.conditions import LaunchConfigurationEquals

def generate_launch_description():

    pmb2_laser_sensors_dir = get_package_share_directory('pmb2_laser_sensors')
    laser = LaunchConfiguration('laser')

    declare_laser_cmd = DeclareLaunchArgument(
		'laser', default_value='sick-561',
		description='Specify the type of laser in the robot'
	)

    laser_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(PathJoinSubstitution(
            substitutions=[pmb2_laser_sensors_dir, "launch",
                PythonExpression(['"', LaunchConfiguration("laser"), '_laser.launch.py"'])]))
    )

    laser_config_path = PathJoinSubstitution(
            substitutions=[pmb2_laser_sensors_dir, "config",
                PythonExpression(['"', LaunchConfiguration("laser"), '_filter.yaml"'])])

    laser_filter_node = Node(
        package='laser_filters',
        # name = 'laser_filter',        # Name changed produces multiple nodes with the same name.
                                        # https://answers.ros.org/question/344141/ros2-launch-creates-two-nodes-of-same-type/
        executable='scan_to_scan_filter_chain',
        output='screen',
        remappings=[('scan', 'scan_raw'),
                    ('scan_filtered', 'scan')],
        parameters = [laser_config_path]
    )
    
    # Create the launch description
    ld = LaunchDescription()
    
    # Declare the launch options
    ld.add_action(declare_laser_cmd)

    # Add the actions to launch all of the laser nodes
    ld.add_action(laser_launch)
    ld.add_action(laser_filter_node)

    return ld
