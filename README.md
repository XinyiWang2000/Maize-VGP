# Maize-VGP

## Environment
- The following are the environments we have tested, but they are not the only options. Please refer to [NVIDIA/pix2pixHD](https://github.com/NVIDIA/pix2pixHD) for detailed environment configuration.
- Linux
- Python3
- NVIDIA GPU (11G memory or larger) + CUDA10.1 + cuDNN7.6.2


### Installation
- Clone this repo:
```bash
git clone https://github.com/XinyiWang2000/Maize-VGP
cd Maize-VGP
```
- Install PyTorch1.6.0 and dependencies from http://pytorch.org
- Install python packages
```bash
pip install -r requirements.txt
```


### Dataset
To train a model using abundant crop images, please visit our [official website](http://plantphenomics.hzau.edu.cn/journalism)
After downloading, please put the images under the `datasets` folder in the following structure:
```bash
datasets/
├── train_A/
│   ├── image1
│   └── image2
├── train_B/
│   ├── target_image1
│   └── target_image2
├── test_A/
│   ├── image3
│   └── image4
└── test_B/
    ├── target_image3
    └── target_image4
```


### Training example
Train a model at 1024 x 1024 resolution:
```bash
python train.py --name taskname --ngf 64 --label_nc 0 --no_instance --gpu_ids 0 --fineSize 1024 --dataroot ./datasets --nThreads 4 --tf_log --display_winsize 1024 --resize_or_crop resize_or_crop --batchSize 1 --save_epoch_freq 10
```
To view training results, please checkout intermediate results in `./checkpoints/taskname`.


### Testing example
```bash
python test.py --name taskname --ngf 64 --label_nc 0 --no_instance --how_many 20 --dataroot ./datasets --gpu_ids 0 --which_epoch 100
```
The test results will be saved to: `./results/taskname`.


### Perception loss modification
To optimize maize perception loss by using [maize-vgg19](https://drive.google.com/file/d/12hgENj8sAnJzZJfy_OvbDGXFQiHW4Xps/view?usp=drive_link). This is a 6-class classification model for maize period.

## Acknowledgments
The code is mainly referenced from [NVIDIA/pix2pixHD](https://github.com/NVIDIA/pix2pixHD).
