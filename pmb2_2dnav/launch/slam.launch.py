# Copyright (c) 2025 PAL Robotics S.L. All rights reserved.
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

from launch import LaunchDescription
from launch_ros.actions import Node
from launch_pal import get_pal_configuration


def generate_launch_description():

    ld = LaunchDescription()

    slam_toolbox_node = 'slam_toolbox'
    map_saver_node = 'map_saver'
    lifecycle_manager_node = 'lifecycle_manager_slam'

    slam_toolbox_config = get_pal_configuration(
        pkg='slam_toolbox',
        node=slam_toolbox_node,
        ld=ld,
        cmdline_args=['use_sim_time'],
    )
    map_saver_config = get_pal_configuration(
        pkg='nav2_map_server',
        node=map_saver_node,
        ld=ld,
        cmdline_args=['use_sim_time'],
    )
    lifecycle_manager_config = get_pal_configuration(
        pkg='nav2_lifecycle_manager',
        node=lifecycle_manager_node,
        ld=ld,
        cmdline_args=['use_sim_time'],
    )

    slam_toolbox = Node(
        package='slam_toolbox',
        executable='sync_slam_toolbox_node',
        name=slam_toolbox_node,
        output='screen',
        emulate_tty=True,
        parameters=slam_toolbox_config['parameters'],
        remappings=slam_toolbox_config['remappings'],
    )

    map_saver = Node(
        package='nav2_map_server',
        executable='map_saver_server',
        name=map_saver_node,
        output='screen',
        emulate_tty=True,
        parameters=map_saver_config['parameters'],
        remappings=map_saver_config['remappings'],
    )

    lifecycle_manager = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name=lifecycle_manager_node,
        output='screen',
        emulate_tty=True,
        parameters=lifecycle_manager_config['parameters'],
        remappings=lifecycle_manager_config['remappings'],
    )

    ld.add_action(slam_toolbox)
    ld.add_action(map_saver)
    ld.add_action(lifecycle_manager)
    return ld
