cmake_minimum_required(VERSION 3.8)
project(pmb2_rgbd_sensors)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

if(pal_navigation_cfg_cmake_FOUND)
  pal_navigation_cfg_register_pipeline(pipeline/00_rgbd_cobra_realsense-d435.yaml
                      pipeline/00_rgbd_cobra_realsense-d435i.yaml
                      pipeline/00_rgbd_cobra_structure.yaml)
  pal_navigation_cfg_register_variables(variables/10_rgbd_variables.yaml)
elseif(DEFINED ENV{PAL_DISTRO})
  message(FATAL_ERROR "The pal_navigation_cfg_cmake package was not found. Pipelines not registered.")
endif()
if(pal_module_cmake_FOUND)
  pal_register_modules(module/10_rgbd.yaml)
elseif(DEFINED ENV{PAL_DISTRO})
  message(FATAL_ERROR "The pal_module_cmake package was not found. Modules not registered.")
endif()

if(BUILD_TESTING)
  ament_auto_find_test_dependencies()
  ament_lint_auto_find_test_dependencies()
endif()

ament_auto_package()