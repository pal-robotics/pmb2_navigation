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

import os

from ament_index_python import get_package_share_directory

from dataclasses import dataclass

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import UnlessCondition, IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

from launch_pal import get_pal_configuration
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.pal_parameters import load_pal_robot_info
from launch_pal.robot_arguments import CommonArgs


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    namespace: DeclareLaunchArgument = CommonArgs.namespace
    advanced_navigation: DeclareLaunchArgument = CommonArgs.advanced_navigation
    use_sim_time: DeclareLaunchArgument = CommonArgs.use_sim_time


def generate_launch_description():

    # Create the launch description and populate
    ld = LaunchDescription()
    launch_arguments = LaunchArguments()

    launch_arguments.add_to_launch_description(ld)

    declare_actions(ld, launch_arguments)

    return ld


def declare_actions(
    launch_description: LaunchDescription, launch_args: LaunchArguments
):
    map_server_node = 'map_server'
    amcl_node = 'amcl'
    lifecycle_manager_node = 'lifecycle_manager_localization'

    robot_info = load_pal_robot_info()

    adv_nav = robot_info.get('advanced_navigation')
    advanced_navigation = (
        LaunchConfiguration('advanced_navigation') if adv_nav is None
        else ('true' if adv_nav else 'false'))

    ns = robot_info.get('namespace')
    namespace = LaunchConfiguration('namespace') if ns is None else ns

    sim = robot_info.get('use_sim_time')
    use_sim_time = LaunchConfiguration('use_sim_time') if sim is None else sim

    map_server_config = get_pal_configuration(
        pkg='nav2_map_server',
        node=map_server_node,
        ld=launch_description,
        cmdline_args=None,
    )
    map_server_config['parameters'].append({'use_sim_time': use_sim_time})
    amcl_config = get_pal_configuration(
        pkg='nav2_amcl',
        node=amcl_node,
        ld=launch_description,
        cmdline_args=None,
    )
    amcl_config['parameters'].append({'use_sim_time': use_sim_time})
    lifecycle_manager_config = get_pal_configuration(
        pkg='nav2_lifecycle_manager',
        node=lifecycle_manager_node,
        ld=launch_description,
        cmdline_args=None,
    )
    lifecycle_manager_config['parameters'].append({'use_sim_time': use_sim_time})

    map_server = Node(
        namespace=namespace,
        package='nav2_map_server',
        executable='map_server',
        name=map_server_node,
        output='screen',
        emulate_tty=True,
        parameters=map_server_config['parameters'],
        remappings=map_server_config['remappings'],
        condition=UnlessCondition(advanced_navigation)
    )

    launch_description.add_action(map_server)

    amcl = Node(
        namespace=namespace,
        package='nav2_amcl',
        executable='amcl',
        name=amcl_node,
        output='screen',
        emulate_tty=True,
        parameters=amcl_config['parameters'],
        remappings=amcl_config['remappings'],
    )

    launch_description.add_action(amcl)

    amcl_initializer = Node(
        namespace=namespace,
        package='pal_localization_manager_utils',
        executable='amcl_initializer_node',
        name='amcl_initializer',
        output='screen',
        emulate_tty=True,
        parameters=[{
            'use_sim_time': use_sim_time,
            'global_frame_id': 'map',
        }],
        condition=IfCondition(advanced_navigation),
    )

    launch_description.add_action(amcl_initializer)

    lifecycle_manager = Node(
        namespace=namespace,
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name=lifecycle_manager_node,
        output='screen',
        emulate_tty=True,
        parameters=lifecycle_manager_config['parameters'],
        remappings=lifecycle_manager_config['remappings'],
    )

    launch_description.add_action(lifecycle_manager)

    nav2_analyzer = Node(
        package='diagnostic_aggregator',
        executable='add_analyzer',
        namespace='pmb2_2dnav',
        output='screen',
        emulate_tty=True,
        parameters=[
            os.path.join(
                get_package_share_directory('pmb2_2dnav'), 'config', 'nav2_analyzers.yaml')],
    )
    launch_description.add_action(nav2_analyzer)
