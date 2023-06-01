# Copyright (c) 2022 PAL Robotics S.L. All rights reserved.
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
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    """Launch Sim specifics applications (typically the ones in startups)."""
    pmb2_2dnav = get_package_share_directory("pmb2_2dnav")
    pmb2_laser_sensors = get_package_share_directory("pmb2_laser_sensors")
    nav_cfg_monitor = get_package_share_directory("pal_navigation_cfg_monitor")

    # Common Nav Applications Sim + Robot
    pmb2_nav_bringup_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pmb2_2dnav, 'launch', 'pmb2_nav_bringup.launch.py')
        ),
    )

    # Add below your Sim only Nav Application
    # Laser Filters
    laser_filters_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            pmb2_laser_sensors, 'launch', 'laser_filters.launch.py')]
        )
    )

    # Navigation Configuration Monitor
    nav_cfg_monitor_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            nav_cfg_monitor, 'launch', 'navigation_cfg_monitor.launch.py')]
        )
    )

    # Create the launch description and populate
    ld = LaunchDescription()
    ld.add_action(pmb2_nav_bringup_launch)
    ld.add_action(laser_filters_launch)
    ld.add_action(nav_cfg_monitor_launch)

    return ld
