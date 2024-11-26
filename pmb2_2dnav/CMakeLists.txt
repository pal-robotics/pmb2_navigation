cmake_minimum_required(VERSION 3.5)
project(pmb2_2dnav)

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

if(pal_navigation_cfg_cmake_FOUND)
  pal_navigation_cfg_register_pipeline(pipeline/00_localization.yaml
                      pipeline/00_localization_w_composition.yaml
                      pipeline/00_navigation.yaml
                      pipeline/00_navigation_w_composition.yaml
                      pipeline/00_slam.yaml)
  pal_navigation_cfg_register_variables(variables/00_pmb2_variables.yaml)
elseif(DEFINED ENV{PAL_DISTRO})
  message(FATAL_ERROR "The pal_navigation_cfg_cmake package was not found. Pipelines not registered.")
endif()
if(pal_module_cmake_FOUND)
  pal_register_modules(module/00_localization.yaml
                      module/00_navigation.yaml
                      module/00_slam.yaml)
elseif(DEFINED ENV{PAL_DISTRO})
  message(FATAL_ERROR "The pal_module_cmake package was not found. Modules not registered.")
endif()

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_auto_package(INSTALL_TO_SHARE config launch)
