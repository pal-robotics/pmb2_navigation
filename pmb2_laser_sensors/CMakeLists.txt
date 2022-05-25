cmake_minimum_required(VERSION 3.5)
project(pmb2_laser_sensors)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

foreach(dir config launch)
    install(DIRECTORY ${dir}/
        DESTINATION share/${PROJECT_NAME}/${dir})
endforeach()

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_auto_package()
