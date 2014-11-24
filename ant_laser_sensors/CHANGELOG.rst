^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package ant_laser_sensors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

0.9.3 (2014-11-24)
------------------

0.9.2 (2014-11-18)
------------------

0.9.1 (2014-11-18)
------------------
* adds missed rplidar_ros run depend
* fixes rgbd cloud and depth to laser scan nodelets
* fixes node name
* uses floor_filter_xtion/filtered_cloud for rgbd
* uses both depthimage and pointcloud to laserscan
  also includes nodelet versions
* fixes rgbd laser config
* updates frame and topic names
* uses all (240) row pixels to generate the scan
* sets clear_params = true
* comments out the hostname in order to use USB
  this needs the udev rule in the udev folder of this pkg
* renames TiM511 to TiM551 (the right name)
* fixes yaml files paths in the launch files
* adds run dependency on sick_tim3xx
* uses SICK TiM511 laser and renames files
* fixes the launch name
* adds Rebujito laser configuration (+-65deg aperture)
* adds rgbd_laser using depthimage_to_laserscan for the xtion RGBD sensor
* adds rplidar yaml and launch
* reduces laser beamwidth to +-90deg
* refs #8302 : adds sick laser launch and yaml
* refs #8173, #8092 : uses config for hokuyo laser (validates sensor)
* refs #8173 : ant_laser_sensors done
* Contributors: Enrique Fernandez
