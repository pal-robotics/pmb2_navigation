^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package pmb2_laser_sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------

0.13.6 (2018-04-24)
-------------------

0.13.5 (2018-04-17)
-------------------

0.13.4 (2018-04-12)
-------------------

0.13.3 (2018-04-06)
-------------------

0.13.2 (2018-03-08)
-------------------
* Merge branch 'restore-old-hokuyo-node' into 'dubnium-devel'
  Revert "replace hokuyo_node with urg_node"
  See merge request robots/pmb2_navigation!12
* Revert "replace hokuyo_node with urg_node"
  This reverts commit 97a9bbe24e1efbbca6cd59c54acd5b99bbc4ce7c.
* Contributors: Procópio Stein, Victor Lopez

0.13.1 (2018-02-15)
-------------------

0.13.0 (2018-02-01)
-------------------
* Merge branch 'urg-node-driver' into 'dubnium-devel'
  replace hokuyo_node with urg_node
  See merge request robots/pmb2_navigation!10
* replace hokuyo_node with urg_node
* Contributors: Procópio Stein

0.12.0 (2017-10-17)
-------------------

0.11.10 (2017-09-27)
--------------------
* added rgbd scan related files
* normalized package.xml for all packages
* Contributors: Procópio Stein

0.11.9 (2017-09-19)
-------------------

0.11.8 (2017-09-18)
-------------------

0.11.7 (2017-08-08)
-------------------
* updated launch params to match tiago's
* change default laser to sick_tim561
* cosmetic
* Contributors: Procópio Stein

0.11.6 (2017-07-03)
-------------------
* increased lasers fov
* Contributors: Procópio Stein

0.11.5 (2017-06-30)
-------------------

0.11.4 (2017-06-30)
-------------------

0.11.3 (2017-06-01)
-------------------

0.11.2 (2017-04-25)
-------------------

0.11.1 (2017-04-22)
-------------------
* moved filter launch to base launch
* added filter to hokuyo launch file
* Contributors: Procópio Stein

0.11.0 (2017-02-28)
-------------------
* 0.10.4
* changelogs
* Contributors: Procópio Stein

0.10.4 (2017-02-28)
-------------------

0.10.3 (2017-02-24)
-------------------

0.10.2 (2017-02-23)
-------------------
* added dependency to pal_filters
* Contributors: Procópio Stein

0.10.1 (2017-02-23)
-------------------
* removed rgbd related files
* replaced dependency of pal_laser_filters to laser_filters
* normalized and updated laser files
* fix sick laser launch files
* Contributors: Jeremie Deray, Procópio Stein

0.10.0 (2016-03-15)
-------------------
* load laser model on param srv
* Contributors: Jeremie Deray

0.9.15 (2016-03-10)
-------------------

0.9.14 (2016-03-02)
-------------------
* rm usuless deps rplidar
* Contributors: Jeremie Deray

0.9.13 (2016-02-10)
-------------------
* revert sick tim561 time offset
* Contributors: Jeremie Deray

0.9.12 (2016-02-10)
-------------------
* fixed time_offset for tim 561
* Contributors: Procopio Stein

0.9.11 (2016-02-09)
-------------------
* launch the laser based on argument "laser"
* added launch of tim571 and modified 551 for driver sick_tim
* Contributors: Sergio Ramos

0.9.10 (2016-02-09)
-------------------
* update pmb2 laser pkg.xml
* uses sick_tim pkg rather than old version
* added support for sick tim561
* Contributors: Jeremie Deray

0.9.9 (2015-10-26)
------------------

0.9.8 (2015-10-01)
------------------
* change hokuyo port
* laser.launch param to choose hokuyo or sick
* rm rebujito_laser
* Contributors: Jeremie Deray

0.9.7 (2015-02-02)
------------------
* Replace ant -> pmb2
* Rename files
* Contributors: Enrique Fernandez
