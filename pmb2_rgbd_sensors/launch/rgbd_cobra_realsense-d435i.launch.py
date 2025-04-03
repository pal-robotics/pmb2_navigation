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

import rclpy
from rclpy.node import Node as RclpyNode
from launch import LaunchDescription
from launch_ros.actions import LoadComposableNodes, Node
from launch_ros.descriptions import ComposableNode
from launch_pal import get_pal_configuration


def generate_launch_description():

    ld = LaunchDescription()

    base_camera_node = 'base_rgbd_camera'
    roof_camera_node = 'roof_rgbd_camera'
    base_camera_config = get_pal_configuration(
        pkg='realsense_camera_cfg',
        node=base_camera_node,
        ld=ld,
        cmdline_args=False,
    )
    roof_camera_config = get_pal_configuration(
        pkg='realsense_camera_cfg',
        node=roof_camera_node,
        ld=ld,
        cmdline_args=False,
    )

    # If the container node already exists, just load the component
    rclpy.init()
    node = RclpyNode('node_checker')
    rclpy.spin_once(node, timeout_sec=1.0)
    if 'rgbd_container' not in node.get_node_names():
        rgbd_container = Node(
            name='rgbd_container',
            package='rclcpp_components',
            executable='component_container',
            emulate_tty=True,
            output='screen',
        )
        ld.add_action(rgbd_container)
    rclpy.shutdown()

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

    ld.add_action(camera_components)
    return ld
