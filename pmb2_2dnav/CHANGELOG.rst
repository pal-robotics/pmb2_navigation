^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pmb2_2dnav
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.11.0 (2017-02-28)
-------------------
* removed legacy move_base configs
* updated costmap files to match template
* fixed global planner config file
* updated rviz navigation config
* 0.10.4
* changelogs
* updated costmap and recovery params
* fixed robot radius
* Contributors: Procópio Stein

0.10.4 (2017-02-28)
-------------------
* updated costmap and recovery params
* fixed robot radius
* Contributors: Procópio Stein

0.10.3 (2017-02-24)
-------------------
* enhanced navigation config, fixed recovery behaviors
* Contributors: Procópio Stein

0.10.2 (2017-02-23)
-------------------

0.10.1 (2017-02-23)
-------------------
* removed rgbd launches and config, fixed dependencies
* minor changes in mapping and localization config
* better mapping and slam configurations
* updated local_planner config for enhanced version of planner
* updated costmap config based on new tiago files
* add rviz launch file
* Contributors: Jeremie Deray, Procópio Stein

0.10.0 (2016-03-15)
-------------------
* use degree
* Contributors: Jeremie Deray

0.9.15 (2016-03-10)
-------------------
* missing deps maps
* Contributors: Jeremie Deray

0.9.14 (2016-03-02)
-------------------

0.9.13 (2016-02-10)
-------------------

0.9.12 (2016-02-10)
-------------------

0.9.11 (2016-02-09)
-------------------

0.9.10 (2016-02-09)
-------------------
* final review of parameters with jeremie
* restoring plugins in costmaps (but commented)
* correcting errors in pm2_2dnav
  restored amcl laser range to default values, corrected typo in local costmap, removed plugins example
* minor cleaning in pmb2 navigation files
* cleaned generic pmb2_2dnav and improved specific pmb2_5_2dnav
* Contributors: Procopio Stein, procopiostein

0.9.9 (2015-10-26)
------------------
* disable free space mapping for pmb2 & add warning abt it
* Fixing localization amcl jumps
* update rviz conf
* Custom launch file for pmb2-5
* Contributors: Jeremie Deray, Luca Marchionni

0.9.8 (2015-10-01)
------------------
* typo
* add slam graph display to rviz
* amcl laser min/max range
* karto laser max_range
* karto map free space
* reduce global inflation radius
* reduce visualization pub rate
* amcl config add param defaut value + comments
* rviz do not display sonar/rgbd related stuff
* do not launch xtion related stuff
* deactivate rgbd layer for costmaps
* Add laser classification displays
* Sync filter script with ant
* Sync with ant_2dnav
* Add covariance (odometry + pose) displays
  NOTE they are disabled by default because they have some issues yet
  with the 6DOF mode property, which is not disabled properly on startup
* Update layout and add inertia + CoM marker
* Update rviz layout
* Increase the number of sonars from 3 to 5
* Contributors: Enrique Fernandez, Jeremie Deray

0.9.7 (2015-02-02)
------------------
* Replace ant -> pmb2
* Rename files
* Contributors: Enrique Fernandez
