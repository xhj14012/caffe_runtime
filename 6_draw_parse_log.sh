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
if [ ! -d $GLOG ];then
      mkdir -p $GLOG
fi

if [ ! -d result ];then
      mkdir -p result
fi

rm -rf result
mkdir result

python $EXTRATOOLS/parse_log.py $LOG ./
python $EXTRATOOLS/plot_training_log.py.example 0  ./result/0_Test_accuracy_vs_Iters.png $LOG
# python $EXTRATOOLS/parse_log.py $LOG ./
# python $EXTRATOOLS/plot_training_log.py.example 1  ./result/1_Test_accuracy_vs_Seconds.png $LOG
python $EXTRATOOLS/parse_log.py $LOG ./
python $EXTRATOOLS/plot_training_log.py.example 2  ./result/2_Test_loss_vs_Iters.png $LOG
# python $EXTRATOOLS/parse_log.py $LOG ./
# python $EXTRATOOLS/plot_training_log.py.example 3  ./result/3_Test_loss_vs_Seconds.png $LOG
# python $EXTRATOOLS/parse_log.py $LOG ./
# python $EXTRATOOLS/plot_training_log.py.example 4  ./result/4_Train_learning_rate_vs_Iters.png $LOG
# python $EXTRATOOLS/parse_log.py $LOG ./
# python $EXTRATOOLS/plot_training_log.py.example 5  ./result/5_Train_learning_rate_vs_Seconds.png $LOG
# python $EXTRATOOLS/parse_log.py $LOG ./
# python $EXTRATOOLS/plot_training_log.py.example 6  ./result/6_Train_loss_vs_Iters.png $LOG
# python $EXTRATOOLS/parse_log.py $LOG ./
# python $EXTRATOOLS/plot_training_log.py.example 7  ./result/7_Train_loss_vs_Seconds.png $LOG


rm -f *.train
rm -f *.test


echo "Done."

read -n 1 -p "Press any key to continue..." INP
if [ $INP != '' ] ; then
        echo -ne '\b \n'
fi