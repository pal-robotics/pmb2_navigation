#!/bin/bash

if [[ $# < 2 ]]
then
    echo "Usage: $0 <input bag> <output bag>"
    exit 1
fi

INPUT=$1
OUTPUT=$2

rosbag filter $INPUT $OUTPUT "topic != '/tf' or m.transforms[0].header.frame_id != 'map' and m.transforms[0].child_frame_id != 'odom'"
