#!/usr/bin/env sh
set -e
TOOLS=$CAFFE_ROOT/build/tools/Release
EXTRATOOLS=./extra
GLOG=./glog
LOG=$GLOG/image_enhance_tool.log
if [ ! -d $GLOG ];then
	mkdir -p $GLOG
fi

# Enhance image dataset
echo "Split dataset into train and val .."
GLOG_logtostderr=0 GLOG_log_dir=$GLOG \
	python $EXTRATOOLS/image_enhance_tool.py \
	./data  2>&1 | tee $LOG
echo "finished"

read -n 1 -p "Press any key to continue..." INP
if [ $INP != '' ] ; then
	echo -ne '\b \n'
fi