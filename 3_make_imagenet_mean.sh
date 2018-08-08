#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12
# project=init
# EXAMPLE=$CAFFE_ROOT/data/$project
# EXAMPLE=..
# DATA=$CAFFE_ROOT/data/$project
GLOG=./glog
if [ ! -d $GLOG ];then
      mkdir -p $GLOG
fi

LMDB=./lmdb
MEAN=./mean
# DATA=..
TOOLS=$CAFFE_ROOT/build/tools/Release
if [ ! -d $MEAN ];then
      mkdir -p $MEAN
fi

GLOG_logtostderr=0 GLOG_log_dir=$GLOG \
$TOOLS/compute_image_mean $LMDB/train_lmdb \
  $MEAN/mean.binaryproto

echo "Done."

read -n 1 -p "Press any key to continue..." INP
if [ $INP != '' ] ; then
        echo -ne '\b \n'
fi