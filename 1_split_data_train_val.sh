#!/usr/bin/env sh
set -e
TOOLS=$CAFFE_ROOT/build/tools/Release
EXTRATOOLS=./extra
GLOG=./glog
LOG=$GLOG/split_data_train_val.log
if [ ! -d $GLOG ];then
	mkdir -p $GLOG
fi

# Split dataset into train and val
echo "Split dataset into train and val .."
GLOG_logtostderr=0 GLOG_log_dir=$GLOG \
	python $EXTRATOOLS/create_train_val_split.py \
	--valRatio 0.3 \
	./data  2>&1 | tee $LOG
echo "finished"

# Generate train.txt
echo "Generate train.txt .."
GLOG_logtostderr=0 GLOG_log_dir=$GLOG \
python $EXTRATOOLS/create_pathfile_train_txt.py \
	2>&1 | tee $LOG
echo "finished"

# Generate tval.txt
echo "Generate tval.txt .."
GLOG_logtostderr=0 GLOG_log_dir=$GLOG \
python $EXTRATOOLS/create_pathfile_val_txt.py \
	2>&1 | tee $LOG
echo "finished"

read -n 1 -p "Press any key to continue..." INP
if [ $INP != '' ] ; then
	echo -ne '\b \n'
fi