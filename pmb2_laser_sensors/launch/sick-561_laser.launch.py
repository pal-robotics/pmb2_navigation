# Copyright (c) 2023 PAL Robotics S.L. All rights reserved.
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
from launch_ros.actions import Node


def generate_launch_description():
    pmb2_laser_sensors_dir = get_package_share_directory("pmb2_laser_sensors")

    node = Node(
        package="sick_tim",
        name="sick_tim_561_ros_driver",
        executable="sick_tim551_2050001",
        output="screen",
        remappings=[("scan", "scan_raw")],
        parameters=[
            os.path.join(
                pmb2_laser_sensors_dir, "config", "sick_tim561_laser.yaml"
            )
        ],
    )

    # Create the launch description
    ld = LaunchDescription()

    # Add the node with the driver for the laser
    ld.add_action(node)

    return ld
