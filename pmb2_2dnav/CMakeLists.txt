cmake_minimum_required(VERSION 3.5)
project(pmb2_2dnav)

find_package(ament_cmake_auto REQUIRED)

# PAL Robotics stricter build flags, other developers should not worry about
# this
find_package(ament_cmake_pal QUIET)

ament_auto_find_build_dependencies()

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

install(PROGRAMS scripts/record_mapping.sh
          scripts/record_move_base.sh
          scripts/record_odom.sh
          scripts/record_patrol.sh
          scripts/record_rgbd.sh
        DESTINATION lib/${PROJECT_NAME})

ament_auto_package(INSTALL_TO_SHARE config launch params)
