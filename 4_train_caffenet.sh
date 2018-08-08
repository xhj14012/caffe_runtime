#!/usr/bin/env sh
set -e
TOOLS=$CAFFE_ROOT/build/tools/Release
GLOG=./glog
LOG=$GLOG/train.log
if [ ! -d $GLOG ];then
	mkdir -p $GLOG
fi
GLOG_logtostderr=0 GLOG_log_dir=$GLOG \
$TOOLS/caffe train \
	--solver=./models/caffenet/solver.prototxt \
	2>&1 | tee $LOG

read -n 1 -p "Press any key to continue..." INP
if [ $INP != '' ] ; then
	echo -ne '\b \n'
fi