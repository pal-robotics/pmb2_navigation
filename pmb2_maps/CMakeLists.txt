cmake_minimum_required(VERSION 3.5)
project(pmb2_maps)

find_package(ament_cmake_auto REQUIRED)

# PAL Robotics stricter build flags, other developers should not worry about this
find_package(ament_cmake_pal QUIET)
 
ament_auto_find_build_dependencies()

ament_auto_package(INSTALL_TO_SHARE config configurations)
# Pending to migrate building info to ROS2
# buildings  building_description.yaml building.yaml)
