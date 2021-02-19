# SoloCell
A Cell Instance Segmentation Tool using SOLOv2.

## Quick Start

### Requirements
- Linux (Windows is not officially supported)
- Python 3.5+
- PyTorch 1.1 or higher (>=1.5 is not tested)
- CUDA 9.0 or higher
- NCCL 2
- GCC 4.9 or higher
- [mmcv 0.2.16](https://github.com/open-mmlab/mmcv/tree/v0.2.16)

or use the provided yaml file [solov2-pytorch1.4-environment.yaml](Environment/solov2-pytorch1.4-environment.yaml)(Python = 3.7, Pytorch = 1.4, Cuda = 10.1, GCC = 5.5).

### Download SoloCell
```shell
git-lfs clone https://github.com/Liuzhe30/SoloCell
```

### Install [SOLO](https://github.com/WXinlong/SOLO)
SOLOv2 implementation is based on [mmdetection](https://github.com/open-mmlab/mmdetection)(v1.0.0). Please refer to the [official document](https://github.com/WXinlong/SOLO/blob/master/docs/INSTALL.md) for installation.

a. Create a conda virtual environment and activate it.

```shell
conda create -n solo python=3.7 -y
conda activate solo
```

b. Install PyTorch and torchvision following the [official instructions](https://pytorch.org/), e.g.,

```shell
conda install pytorch torchvision -c pytorch
```

c. Clone the SOLO repository.

```shell
git clone https://github.com/WXinlong/SOLO.git
cd SOLO
```

d. Install build requirements and then install SOLO.
(We install pycocotools via the github repo instead of pypi because the pypi version is old and not compatible with the latest numpy.)

```shell
pip install -r requirements/build.txt
pip install "git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI"
pip install -v -e .  # or "python setup.py develop"
```

### Dataset Preparation
```shell
python3 mask_recreator.py
```
If you want to recreate the annotation files, please run the following commands:
```shell
python3 mask_annotation.py
python3 mask_pycococreator.py
```

## Usage
### Train with single GPU
```shell
cd SOLO
python tools/train.py ${CONFIG_FILE}

Example:
python tools/train.py configs/solo/solov2_r50_fpn_8gpu_1x_cellpose.py
```

## Contributing to the project
Any pull requests or issues are welcome.

## Progress
- [x] README for running SoloCell.