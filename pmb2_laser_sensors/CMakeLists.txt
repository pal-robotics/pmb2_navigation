cmake_minimum_required(VERSION 3.5)
project(pmb2_laser_sensors)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

if(pal_navigation_cfg_cmake_FOUND)
  pal_navigation_cfg_register_pipeline(pipeline/00_laser_hokuyo.yaml
                      pipeline/00_laser_sick-561.yaml
                      pipeline/00_laser_sick-571.yaml
                      pipeline/00_laser_sim.yaml
                      pipeline/00_laser_w_composition_hokuyo.yaml
                      pipeline/00_laser_w_composition_sick-561.yaml
                      pipeline/00_laser_w_composition_sick-571.yaml)
  pal_navigation_cfg_register_variables(variables/10_hokuyo_variables.yaml
                      variables/10_sick_variables.yaml)
elseif(DEFINED ENV{PAL_DISTRO})
  message(FATAL_ERROR "The pal_navigation_cfg_cmake package was not found. Pipelines not registered.")
endif()
if(pal_module_cmake_FOUND)
  pal_register_modules(module/00_laser.yaml)
elseif(DEFINED ENV{PAL_DISTRO})
  message(FATAL_ERROR "The pal_module_cmake package was not found. Modules not registered.")
endif()

if(BUILD_TESTING)
  ament_auto_find_test_dependencies()
  ament_lint_auto_find_test_dependencies()
endif()

ament_auto_package()
