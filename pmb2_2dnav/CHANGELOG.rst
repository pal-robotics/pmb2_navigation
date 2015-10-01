^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pmb2_2dnav
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
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
