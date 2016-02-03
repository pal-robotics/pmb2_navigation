cmake_minimum_required(VERSION 2.8.3)
project(pmb2_7_2dnav)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY 
config
DESTINATION ${CATKIN_GLOBAL_SHARE_DESTINATION}/pmb2_2dnav)
