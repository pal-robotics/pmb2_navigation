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
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch.conditions import UnlessCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    """Launch Sim specifics applications (typically the ones in startups)."""
    ld = LaunchDescription()

    pmb2_2dnav = get_package_share_directory("pmb2_2dnav")
    pmb2_laser_sensors = get_package_share_directory("pmb2_laser_sensors")

    declare_is_public_sim_arg = DeclareLaunchArgument(
        "is_public_sim",
        default_value="false",
        description="Whether or not you are using a public simulation",
    )

    # Simulation + Robot Navigation Applications
    # ====================================
    pmb2_nav_bringup_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pmb2_2dnav, "launch", "pmb2_nav_bringup.launch.py")
        ),
    )

    # Simulation Navigation Applications Only
    # =================================
    # Private + Public Simulation
    # ---------------------------
    # Laser Filters
    laser_filters_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [
                os.path.join(
                    pmb2_laser_sensors, "launch", "laser_filters.launch.py"
                )
            ]
        )
    )

    # Private Simulation Only
    # ------------------
    # Can throw if some pkg is not available in public sim
    ld.add_action(declare_is_public_sim_arg)
    try:
        # Navigation Configuration Monitor
        nav_cfg_monitor_launch = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [
                    os.path.join(
                        get_package_share_directory(
                            "pal_navigation_cfg_monitor"
                        ),
                        "launch",
                        "navigation_cfg_monitor.launch.py",
                    )
                ]
            ),
            condition=UnlessCondition(LaunchConfiguration("is_public_sim")),
        )
        ld.add_action(nav_cfg_monitor_launch)
    except Exception:
        pass

    # Create the launch description and populate
    ld.add_action(pmb2_nav_bringup_launch)
    ld.add_action(laser_filters_launch)

    return ld
