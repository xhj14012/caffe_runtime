#!/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs
# project=init
# EXAMPLE=$CAFFE_ROOT/data/$project
#EXAMPLE=..
# DATA=$CAFFE_ROOT/data/$project
DATA=./data
LMDB=./lmdb
TOOLS=$CAFFE_ROOT/build/tools/Release
GLOG=./glog
if [ ! -d $GLOG ];then
      mkdir -p $GLOG
fi
# TRAIN_DATA_ROOT=$CAFFE_ROOT/data/$project/train/
TRAIN_DATA_ROOT=$DATA/train/
# VAL_DATA_ROOT=$CAFFE_ROOT/data/$project/train/
VAL_DATA_ROOT=$DATA/val/

# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
RESIZE=false
if $RESIZE; then
  RESIZE_HEIGHT=300
  RESIZE_WIDTH=300
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

# if [ ! -d "$TRAIN_DATA_ROOT" ]; then
#   echo "Error: TRAIN_DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"
#   echo "Set the TRAIN_DATA_ROOT variable in create_imagenet.sh to the path" \
#        "where the ImageNet training data is stored."
#   exit 1
# fi

# if [ ! -d "$VAL_DATA_ROOT" ]; then
#   echo "Error: VAL_DATA_ROOT is not a path to a directory: $VAL_DATA_ROOT"
#   echo "Set the VAL_DATA_ROOT variable in create_imagenet.sh to the path" \
#        "where the ImageNet validation data is stored."
#   exit 1
# fi

if [ ! -d $LMDB ];then
      mkdir -p $LMDB
fi

rm -rf $LMDB/train_lmdb
rm -rf $LMDB/val_lmdb

echo "Creating train lmdb..."
# rm -rf $LMDB/train_lmdb
GLOG_logtostderr=0 GLOG_log_dir=$GLOG \
$TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $TRAIN_DATA_ROOT \
    $DATA/train.txt \
    $LMDB/train_lmdb

echo "Creating val lmdb..."
# rm -rf $LMDB/val_lmdb
GLOG_logtostderr=0 GLOG_log_dir=$GLOG \
$TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $VAL_DATA_ROOT \
    $DATA/val.txt \
    $LMDB/val_lmdb

echo "Done."

read -n 1 -p "Press any key to continue..." INP
if [ $INP != '' ] ; then
        echo -ne '\b \n'
fi