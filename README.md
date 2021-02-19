# SoloCell
A Cell Instance Segmentation Tool using SOLOv2.

## Quick Start

### Requirements
- Python = 3.7
- Pytorch = 1.4
- Cuda = 10.1
- GCC = 5.5

### Download SoloCell
```
git-lfs clone https://github.com/Liuzhe30/SoloCell
```

### Install [SOLO](https://github.com/WXinlong/SOLO)
SOLOv2 implementation is based on [mmdetection](https://github.com/open-mmlab/mmdetection)(v1.0.0). Please refer to the [official document](https://github.com/WXinlong/SOLO/blob/master/docs/INSTALL.md) for installation, or:
```
cd SOLO
pip install -r requirements/build.txt
pip install "git+https://github.com/cocodataset/cocoapi.git#subdirectory=PythonAPI"
pip install -v -e .  # or "python setup.py develop"
```

### Dataset Preparation
```
python3 mask_recreator.py
```
If you want to recreate the annotation files, please run the following commands:
```
python3 mask_annotation.py
python3 mask_pycococreator.py
```

## Usage
### Train with single GPU
```
python tools/train.py ${CONFIG_FILE}

Example:
python tools/train.py configs/solo/solov2_r50_fpn_8gpu_1x_cellpose.py
```

## Contributing to the project
Any pull requests or issues are welcome.

## Progress
- [x] README for running SoloCell.