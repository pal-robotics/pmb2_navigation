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

    map_server_node = 'map_server'
    map_saver_node = 'map_saver'
    amcl_node = 'amcl'
    lifecycle_manager_node = 'lifecycle_manager_localization'

    map_server_config = get_pal_configuration(
        pkg='nav2_map_server',
        node=map_server_node,
        ld=ld,
        cmdline_args=['use_sim_time'],
    )
    map_saver_config = get_pal_configuration(
        pkg='nav2_map_server',
        node=map_saver_node,
        ld=ld,
        cmdline_args=['use_sim_time'],
    )
    amcl_config = get_pal_configuration(
        pkg='nav2_amcl',
        node=amcl_node,
        ld=ld,
        cmdline_args=['use_sim_time'],
    )
    lifecycle_manager_config = get_pal_configuration(
        pkg='nav2_lifecycle_manager',
        node=lifecycle_manager_node,
        ld=ld,
        cmdline_args=['use_sim_time'],
    )

    map_server = Node(
        package='nav2_map_server',
        executable='map_server',
        name=map_server_node,
        output='screen',
        emulate_tty=True,
        parameters=map_server_config['parameters'],
        remappings=map_server_config['remappings'],
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

    amcl = Node(
        package='nav2_amcl',
        executable='amcl',
        name=amcl_node,
        output='screen',
        emulate_tty=True,
        parameters=amcl_config['parameters'],
        remappings=amcl_config['remappings'],
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

    ld.add_action(map_server)
    ld.add_action(map_saver)
    ld.add_action(amcl)
    ld.add_action(lifecycle_manager)
    return ld
