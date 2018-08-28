# Easycaffe

	this is a small quick start tools set for caffenet(alexnet) model train  and simple validation in industrial environment.

 0. Enhance image(optional)

       Your tagged image data should be prepared like 

       	./data/OK/*.jpg
       	./data/NG/*.jpg
       	./data/*/*.jpg
       Then simply run (test on git-bash)

       ```bash
       source 0_enhance_img.sh
       ```

       You can custom parameters at the beginning of ''./extra/image_enhance_tool.py' , according to the situation.

       Only support jpg(jpeg), bmp,png image format by default, and will all be converted into jpg by default (for the convenience of subsequent operation).

 1. Split data into training set and validation set

      Simply run

      ```bash
      source 1_split_data_train_val.sh
      ```

      your data will be split into train set and val set according to a certain proportion randomly，and the final lists will be save at ./data/train.txt and ./data/val.txt automatically。

      The default proportion is train:val = 0.7:0.3 ,you can custom it in 'split_data_train_val.sh' .

 2. Create imagenet

      Simply run

      ```bash
      source 2_create_imagenet.sh
      ```

      Target imagenet will be save as lmdb format at ./lmdb/train/train_lmdb and ./lmdb/val/val_lmdb .

 3. Make mean file of imagenet

      Simply run

      ```bash
      source 3_make_imagenet_mean.sh
      ```

      Target mean file will be save at ./mean .

      (Remember to recalculate mean value after rebuild imagenet.)

 4. Training caffenet

      Simply run

      ```bash
      source 4_train_caffenet.sh
      ```

      You should custom model files under ./models/ follow the official caffe guide.

 5. Resume training

      Simply run

      ```bash
      source 5_resume_training.sh
      ```

 6. Draw training or test log

      Simply run

      ```bash
      source 6_draw_test_log.sh
      ```

 7. Get model files and Validate

      Caffemodels will all  be in ./models/*/ .

      You also need 

      ```bash
      ./models/*/*.deploy.prototxt
      ./mean/mean.binaryproto
      labels.txt
      ```

      to get caffemodel into validate and use.