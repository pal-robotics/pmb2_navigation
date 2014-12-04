^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ant_2dnav
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* Add debug param to RGBD source
* Update record scripts
* Set combination method to max for RGBD
* Reduces linear speed from 0.5 to 0.3m/s
* Increase rgbd range on costmap
* Adds scan arg
* Contributors: Enrique Fernandez

0.9.3 (2014-11-24)
------------------
* Add missed dependency (pal_local_planner)
* Make pal local planner speed depend on max vel x
* Enable rgbd layer on local costmap
* Reduce raytrace/obstacle range in rgbd layer
* Add missed ant_laser_sensors dependency
* Contributors: Enrique Fernandez

0.9.2 (2014-11-18)
------------------
* disables saving initial_ params
  NOTE this generates 1 socket every time a param is set
* Contributors: Enrique Fernandez

0.9.1 (2014-11-18)
------------------
* adds floor filtered PC
* adds blanking_range = 0.5m to costmap config
* adds floor_filter option arg to move_base
* adds scan arg to mapping_karto
* uses floor_filter_xtion/filtered_cloud for rgbd
* sets frame for pointcloud_to_laserscan
* uses rgbd_scan in costmap_2d
* adds rgbd_scan to rviz
* fixes Pose Graph display
* adds Pose Graph display
* adds state param
* sets debug_rgbd to false by default
  since we don't use a voxel_grid layer for the rgbd, we don't really need
  this!
* adds record scripts
* uses xtion depth points topic
* refs #10175 : uses navigation.sh
* updates marking/clearing ranges for xtion pro live
* takes pose.yaml from $HOME
* sets robot = ant for the state machine
* takes maps from $HOME/.pal/ant_maps/config
* saves trajectory.yaml in $HOME/.pal folder
* sets SICK TiM511 range for mapping
* uses ObstacleLayer for rgbd (as in global costmap)
  but still disabled
* global_costmap - use obstacleLayer instead of voxelLayer for obstacle_rgbd_layer
* uses MarkerArray (text + arrow)
* adds inventory group display
* adds compressed map display
* adds voxel grid marker
* adds debug_rgbd with voxel grid markers
* sets softkinetic topic and frame
* updates rgbd camera topic name
* adds heading scoring params (disabled by default for now)
* uses !degrees
* reduces planner frequency (allows for triggering recovery behaviors faster: before 5s, now 2s)
  increases controller frequency to 10s
* adds rgbd layer; disabled by default (for now)
* adds clearing endpoints (for RBGD sensor)
* adds RGBD sensor
* fixes global_costmap configuration
* sets pal local_planner as default one (instead of trajectory)
* sets allow_backwards to false
* adds trajectories marker array
* disables visual localization
* adds pattern cloud
* reduces default_tolerance to 0.0 (exact goal)
  doesn't allow unknown
* reduces inflation to 0.6 (1.0 makes the robot oscillate so much to bad readings)
  disables overwrite with laser on the static_layer (it gets cleared on the robot)
  disables the vo_layer, because it's not been tested on the robot
* reduces dist_to_avoid from 0.85 to 0.25 to alleviate the problem of arriving to the goal with very slow linear speed
* reduces max linear velocity to 0.5 (before was 0.9)
* indentation only
* sets robot width and length correctly and disables crowd
* fixes move_by and move_by_unsafe
  NOTE that it must be run with localization fake!
* renames/fixes obstacle_bumper_layer name
* increases the inflation radius from 0.3 to 1.0
  NOTE this is quite conservative and it will create oscillations in narrow spaces
* goes back to multiple obstacle layers
* formatting only
* adds missing dependencies (gmapping, pal_karto)
* fixes default_tolerance (now works) + visualizes potential
* adds potential
* adds groups to support several global planners
  NOTE navfn and global_planner
* increases pdist_scale from 0.6 to 1.2 to force the robot follow the path more
  NOTE with 1.6 goes even more close to the path, but for that we have to increase
  the inflation to avoid going so close (avoid speed_limit or collisions)
  Before, with 0.6, the dynamics make the robot be faster but going far from the path!
  Also, remember that we set this param and also its redundant version, just in case
* uses degrees 60 instead of 1.0 rad, as for the redundant param
* adds vo_cloud because with combination_method = 0 (overwrite) they're clear!
* puts obstacle_ prefix to obstacle layers
  NOTE this is required for 1.11.8 (and also for the latest, 1.11.9, at this moment)
  because only the layers with obstacle (default) in the name are clear when the
  clear recovery behaviors are called
* adds default_tolerance of 1.0 (default was 0.0) to navfn and global_planner
  NOTE this allows to go up to 1m around a goal
  We need 1.11.10 to try first the exact goal!
* robot radius must be outside inflation_layer
  NOTE it's redundant in the inflation_layer, and it will disappear after '1.11.9'
* refs #9512 : syncs with reem from 4.5_ROBOTICSVA
* creates fake localization params and uses base_footprint
* reduces cost grid alpha from 1.0 to 0.2
* changes to trajectory local planner as default
  instead of PAL
  NOTE that PAL was ok, but the robot moves backwards
  specially when starting a new path
* tunes trajectory planner config
  NOTE follows turtlebot config with some minor changes/tuning
  See:
  https://github.com/turtlebot/turtlebot_apps/blob/hydro/turtlebot_navigation/param/base_local_planner_params.yaml
* tunes planner and controller frequency and patience
  NOTE this makes the trajectory planner work much better
  Configuration follows this one:
  https://github.com/turtlebot/turtlebot_apps/commit/8165cdfcf1afc749b7f8a64cf5dfab398c200a6f
* sets the correct robot and inflation radius
  NOTE the robot_radius (with this navigation stack 1.11.4)
  must be given outside the inflation layer!
* configures cost grid
  NOTE the size of 0.7 makes the flat squares to overlap in
  order to have a nice surf, but there's a bug in rviz which
  doesn't draw these flat squares with the frame orientation,
  so the overlap/size is greater than the one really needed.
* adds local planner cost grid
* uses base_footprint
* uses base_footprint
* uses base_frame = base_footprint
* refs #8895 : uses single sensor_layer
* refs #9368 : reduces range for sonar in local_costmap
* refs #9368 : fixes sonar obstacle/raytrace_range
* syncs with reem_2dnav/launch
* refs #9368 : fixes costmap config
  NOTE syncs with RH* config
* removes unused params and clean style
* uses base_footprint
* re-enables laser in global costmap
  NOTE this is required because otherwise the global planner goes
  straight!
* uses base_footprint and use resolution only once
* disables laser observation in global costmap
* refs #9288 : reduces initial map size
* fixes remap to use scan
* loads last pose
* changes colors for dock cloud
* fixes twist_marker and adds dock pose and cloud
* adds Dock group (to debug docking utils)
* sets buffer length to 3 for sonars
* reduces TF marker scale from 0.3 to 0.1
* updates rviz layout
* syncs with reem_2dnav
  NOTE this fixes the vo_cloud issue that prevented the robot to navigate autonomously
* refs #8447 : syncs 2dnav with reem
  NOTE this uses the layered costmaps
* reduces TF marker scale from 1.0 to 0.3
* updates layout and uses sonar_base (not sonar_torso)
* refs #8173 : updates laser max range for 5.6m
* refs #8317 : uses single rviz layout
* refs #8317 : uses pal_navigation_sm intead of reem_maps
* saves trajectory file (follows -r52013)
* refs #8173 : uses scan (instead of scan_filtered)
* refs #8173 : removes footprint and uses robot radius
* refs #8173 : uses reem_maps for the map.launch file
* refs #8173 : ant_2dnav done
* Contributors: Enrique Fernandez, artivis
