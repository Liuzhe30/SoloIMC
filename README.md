# SoloIMC
An IMC Necleus Instance Segmentation Tool using SOLOv2.
<p align="center"><img width="80%" src="example.png" /></p>

## Quick Start

### Requirements
- Linux (Windows is not officially supported)
- Python 3.5+
- PyTorch 1.1 or higher (>=1.5 is not tested)
- CUDA 9.0 or higher
- NCCL 2
- GCC 4.9 or higher
- [mmcv 0.2.16](https://github.com/open-mmlab/mmcv/tree/v0.2.16)

or use the provided yaml file [solov2-pytorch1.4-environment.yaml](Environment/solov2-pytorch1.4-environment.yaml) (with Python = 3.7, PyTorch = 1.4, CUDA = 10.1, GCC = 5.5).

### Download SoloIMC
```shell
git-lfs clone https://github.com/Liuzhe30/SoloIMC
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
pip install cython
pip install git+git://github.com/waspinator/coco.git@2.1.0
python3 mask_annotation.py
python3 mask_pycococreator.py
```

## Usage
### Train with single GPU
```shell
cd SOLO
python tools/train.py ${CONFIG_FILE}

Example:
python tools/train.py configs/solov2_r50_fpn_8gpu_1x_imc.py
```

### Testing
```shell
# single-gpu testing
python tools/test_ins.py ${CONFIG_FILE} ${CHECKPOINT_FILE} --show --out  ${OUTPUT_FILE} --eval segm

Example: 
python tools/test_ins.py configs/solov2_r50_fpn_8gpu_1x_imc.py  work_dirs/solov2_release_r50_fpn_8gpu_1x/epoch_10.pth --show --out  results_solo.pkl --eval segm
```

### Visualization
```shell
python tools/test_ins_vis.py ${CONFIG_FILE} ${CHECKPOINT_FILE} --show --save_dir  ${SAVE_DIR}

Example: 
python tools/test_ins_vis.py configs/solov2_r50_fpn_8gpu_1x_imc.py  work_dirs/solov2_release_r50_fpn_8gpu_1x/epoch_10.pth --show --save_dir  work_dirs/vis_solo
```

## Contributing to the project
Any pull requests or issues are welcome.

## Progress
- [x] README for running SoloIMC.