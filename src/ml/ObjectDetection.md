On Davinci AI-Core
------------------

* SUpports b8, b16, b32
* Supports Block computing, resambles GPU (ref. BLOCKID register)
* Supports YUV420, XRGB888, AYUV444 formats of data storage
* Concept of Bariers and Pipelines
* Supports compressed data (ZIP/UNZIP commands)

Talked about internal locations called L1, OUT, UB, L0C16, LOC32, L0C16V,
L0C32V. Looks like they associated with im2col format somehow.

LOA,LOB,LOC are the locations of matrices.

(On im2col:
<https://leonardoaraujosantos.gitbooks.io/artificial-inteligence/content/making_faster.html>)

Load instruction uses the following data format: NC1WHC0


Object detection Task
---------------------

Current SOTA models:
- RetinaNET
- HTC

### RetinaNet

* Keras implementation <https://github.com/fizyr/keras-retinanet>
  - Site says, image size is 224x224
* Datasets:
  - Microsoft COCO
    * Site <http://cocodataset.org/#home>
    * Paper <https://arxiv.org/pdf/1405.0312>
    * GitHub <https://github.com/nightrome/cocostuff>
    * Year 2015
    * 91 object types
    * 5K labeled instances of each of 82 of them, total 2.5M labeled instances
    * 328K images
    * ~20K + 10K worker hours
    * Image size is unclear. Probably, 640x480x3
  - Pascal VOC <http://host.robots.ox.ac.uk/pascal/VOC/>

Two aspects over older YOLO models

1. Feature Pyramid Network (FPN)
2. Focal Loss

Inference speed of RetinaNet-101-600 (600 is the size of input picture) is 122ms
per image on NVidia M40 GPU. GPU specs are in <https://www.techpowerup.com/gpu-specs/tesla-m40.c2771>
6.844 TFLOPS

### YOLO9000/Darknet

Paper <https://arxiv.org/pdf/1612.08242>

Speed-oriented model. Reports 67FPS mode. Input image size is 224x224 for YOLO
and 448x448 for YOLOv2. Training process is multy-staged: training phase is
followed by fine-tuning phase.

Darknet-19 is the name of YOLOv2: "Darknet-19 only requires 5.58 billion
operations to process an image yet achieves 72.9% top-1 accuracy and 91.2% top-5
accuracy on ImageNet."

![Darknet19 layers](./img/darknet19_layers.png)


