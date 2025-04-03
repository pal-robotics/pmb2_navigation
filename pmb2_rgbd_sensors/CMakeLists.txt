cmake_minimum_required(VERSION 3.8)
project(pmb2_rgbd_sensors)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

if(pal_module_cmake_FOUND)
  pal_register_modules(module/10_rgbd.yaml)
elseif(DEFINED ENV{PAL_DISTRO})
  message(FATAL_ERROR "The pal_module_cmake package was not found. Modules not registered.")
endif()
if(pal_configuration_cmake_FOUND)
  pal_register_configs(
    CONFIGS
      params/00_rgbd_cobra_realsense-d435_pmb2.yaml
      params/00_rgbd_cobra_realsense-d435i_pmb2.yaml
    RESOURCE_NAME
      realsense_camera_cfg
  )
  pal_register_configs(
    CONFIGS
      params/00_rgbd_cobra_structure_pmb2.yaml
    RESOURCE_NAME
      structure_camera_cfg
  )
elseif(DEFINED ENV{PAL_DISTRO})
  message(FATAL_ERROR "The pal_configuration_cmake package was not found. Configurations not registered.")
endif()

if(BUILD_TESTING)
  ament_auto_find_test_dependencies()
  ament_lint_auto_find_test_dependencies()
endif()

ament_auto_package(INSTALL_TO_SHARE launch)