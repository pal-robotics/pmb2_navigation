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

from dataclasses import dataclass

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import LoadComposableNodes, Node
from launch_ros.descriptions import ComposableNode

from launch_pal import get_pal_configuration
from launch_pal.arg_utils import LaunchArgumentsBase
from launch_pal.robot_arguments import CommonArgs
from launch_pal.conditions import UnlessNodeRunning


@dataclass(frozen=True)
class LaunchArguments(LaunchArgumentsBase):
    namespace: DeclareLaunchArgument = CommonArgs.namespace


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
    base_camera_node = 'base_rgbd_camera'
    roof_camera_node = 'roof_rgbd_camera'
    base_camera_config = get_pal_configuration(
        pkg='realsense_camera_cfg',
        node=base_camera_node,
        ld=launch_description,
        cmdline_args=False,
    )
    roof_camera_config = get_pal_configuration(
        pkg='realsense_camera_cfg',
        node=roof_camera_node,
        ld=launch_description,
        cmdline_args=False,
    )

    # If the container node already exists, just load the component
    rgbd_container = Node(
        name='rgbd_container',
        package='rclcpp_components',
        executable='component_container',
        emulate_tty=True,
        output='screen',
        condition=UnlessNodeRunning('rgbd_container')
    )

    launch_description.add_action(rgbd_container)

    camera_components = LoadComposableNodes(
        target_container='rgbd_container',
        composable_node_descriptions=[
            # Roof Camera Driver
            ComposableNode(
                package='realsense2_camera',
                plugin='realsense2_camera::RealSenseNodeFactory',
                name=roof_camera_node,
                namespace='roof_rgbd_camera',
                parameters=roof_camera_config["parameters"],
                remappings=roof_camera_config["remappings"],
            ),
            # Base Camera Driver
            ComposableNode(
                package='realsense2_camera',
                plugin='realsense2_camera::RealSenseNodeFactory',
                name=base_camera_node,
                namespace='base_rgbd_camera',
                parameters=base_camera_config["parameters"],
                remappings=base_camera_config["remappings"],
            ),
        ],
    )

    launch_description.add_action(camera_components)
