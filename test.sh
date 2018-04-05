#!/bin/bash

WORKSPACE=.
RECORD_PATH=$WORKSPACE/record_`date +"%Y-%m-%d_%H-%M-%S"`
python3 $WORKSPACE/video_recorder.py $RECORD_PATH
