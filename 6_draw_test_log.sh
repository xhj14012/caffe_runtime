#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12
# project=init
# EXAMPLE=$CAFFE_ROOT/data/$project
# EXAMPLE=..
# DATA=$CAFFE_ROOT/data/$project
EXTRATOOLS=./extra
TOOLS=$CAFFE_ROOT/build/tools/Release
GLOG=./glog
LOG=$GLOG/train.log
RESULT=./result
if [ ! -d $GLOG ];then
      mkdir -p $GLOG
fi

if [ ! -d $RESULT ];then
      mkdir -p $RESULT
fi

python $EXTRATOOLS/parse_log.py $LOG ./result
python $EXTRATOOLS/plot_training_log.py.example 0  ./result/0_Test_accuracy_vs_Iters-`date +%Y-%m-%d-%H-%M-%S`.png $LOG
# python $EXTRATOOLS/plot_training_log.py.example 1  ./result/1_Test_accuracy_vs_Seconds-`date +%Y-%m-%d-%H-%M-%S`.png $LOG
python $EXTRATOOLS/plot_training_log.py.example 2  ./result/2_Test_loss_vs_Iters-`date +%Y-%m-%d-%H-%M-%S`.png $LOG
# python $EXTRATOOLS/plot_training_log.py.example 3  ./result/3_Test_loss_vs_Seconds-`date +%Y-%m-%d-%H-%M-%S`.png $LOG



# rm -f *.train
# rm -f *.test


echo "Done."

read -n 1 -p "Press any key to continue..." INP
if [ $INP != '' ] ; then
        echo -ne '\b \n'
fi