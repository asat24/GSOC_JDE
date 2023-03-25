# -*- coding: utf-8 -*-
"""Self Driving Segmentation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HxnWa51cik4-Ecd8w-ngnptGdoABlosA

***Anees  Aslam***

***aneestags786@gmail.com***

***+91 979 115 1535***

<table align="center">
  <td align="center"><a target="_blank" href="https://www.linkedin.com/in/anees-a-5baa4a232/">
        <!-- <img src="https://github.com/asat24/PROJECT/blob/main/Autonomous%20Driving/DP.jpeg" style="height:10px; padding-bottom:10px;" />
      Linkedin</a></td> -->
<td align="center"><a target="_blank" href="https://www.linkedin.com/in/anees-aslam/">
        <img src="data:image/png;base64,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" style="height:10px; padding-bottom:10px;" />
</table>

**IMAGE SEGMENTATION**  *for* **AUTONOMOUS DRIVING**
"""

# Tensorflow
import tensorflow as tf
print(tf.__version__)

# I/O libraries
import os
from io import BytesIO
import tarfile
import tempfile
from six.moves import urllib

# Helper libraries
import matplotlib
from matplotlib import gridspec
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import cv2 as cv
from tqdm import tqdm
import IPython
from sklearn.metrics import confusion_matrix
from tabulate import tabulate

# Comment this out if you want to see Deprecation warnings
import warnings
warnings.simplefilter("ignore", DeprecationWarning)

"""### Build the model

Segmentation results on Flickr images:

<p align="center">
    <img src="https://github.com/tensorflow/models/blob/master/research/deeplab/g3doc/img/vis1.png?raw=true" width=600></br>
    <img src="https://github.com/tensorflow/models/blob/master/research/deeplab/g3doc/img/vis2.png?raw=true" width=600></br>
</p>

In the driving context, we aim to obtain a semantic understanding of the front driving scene throught the camera input. This is important for driving safety and an essential requirement for all levels of autonomous driving. The first step is to build the model and load the pre-trained weights. 

I use the model checkpoint trained on [Cityscapes](https://www.cityscapes-dataset.com/) dataset.

<p align="center">
    <img src="https://www.cityscapes-dataset.com/wordpress/wp-content/uploads/2015/07/muenster00.png" width=600></br>
    <img src="https://www.cityscapes-dataset.com/wordpress/wp-content/uploads/2015/07/zuerich00.png" width=600></br>
</p>

"""

class DeepLabModel(object):
    """Class to load deeplab model and run inference."""

    FROZEN_GRAPH_NAME = 'frozen_inference_graph'

    def __init__(self, tarball_path):
        """Creates and loads pretrained deeplab model."""
        self.graph = tf.Graph()
        graph_def = None

        # Extract frozen graph from tar archive.
        tar_file = tarfile.open(tarball_path)
        for tar_info in tar_file.getmembers():
            if self.FROZEN_GRAPH_NAME in os.path.basename(tar_info.name):
                file_handle = tar_file.extractfile(tar_info)
                graph_def = tf.GraphDef.FromString(file_handle.read())
                break
        tar_file.close()

        if graph_def is None:
            raise RuntimeError('Cannot find inference graph in tar archive.')

        with self.graph.as_default():
            tf.import_graph_def(graph_def, name='')
        self.sess = tf.Session(graph=self.graph)

    def run(self, image, INPUT_TENSOR_NAME = 'ImageTensor:0', OUTPUT_TENSOR_NAME = 'SemanticPredictions:0'):
        """Runs inference on a single image.

        Args:
            image: A PIL.Image object, raw input image.
            INPUT_TENSOR_NAME: The name of input tensor, default to ImageTensor.
            OUTPUT_TENSOR_NAME: The name of output tensor, default to SemanticPredictions.

        Returns:
            resized_image: RGB image resized from original input image.
            seg_map: Segmentation map of `resized_image`.
        """
        width, height = image.size
        target_size = (2049,1025)  # size of Cityscapes images
        resized_image = image.convert('RGB').resize(target_size, Image.ANTIALIAS)
        batch_seg_map = self.sess.run(
            OUTPUT_TENSOR_NAME,
            feed_dict={INPUT_TENSOR_NAME: [np.asarray(resized_image)]})
        seg_map = batch_seg_map[0]  # expected batch size = 1
        if len(seg_map.shape) == 2:
            seg_map = np.expand_dims(seg_map,-1)  # need an extra dimension for cv.resize
        seg_map = cv.resize(seg_map, (width,height), interpolation=cv.INTER_NEAREST)
        return seg_map

"""### Visualization
Now let's create some helper functions for decoding and visualizing the results.
"""

def create_label_colormap():
    """Creates a label colormap used in Cityscapes segmentation benchmark.

    Returns:
        A Colormap for visualizing segmentation results.
    """
    colormap = np.array([
        [128,  64, 128],
        [244,  35, 232],
        [ 70,  70,  70],
        [102, 102, 156],
        [190, 153, 153],
        [153, 153, 153],
        [250, 170,  30],
        [220, 220,   0],
        [107, 142,  35],
        [152, 251, 152],
        [ 70, 130, 180],
        [220,  20,  60],
        [255,   0,   0],
        [  0,   0, 142],
        [  0,   0,  70],
        [  0,  60, 100],
        [  0,  80, 100],
        [  0,   0, 230],
        [119,  11,  32],
        [  0,   0,   0]], dtype=np.uint8)
    return colormap


def label_to_color_image(label):
    """Adds color defined by the dataset colormap to the label.

    Args:
        label: A 2D array with integer type, storing the segmentation label.

    Returns:
        result: A 2D array with floating type. The element of the array
            is the color indexed by the corresponding element in the input label
            to the PASCAL color map.

    Raises:
        ValueError: If label is not of rank 2 or its value is larger than color
            map maximum entry.
    """
    if label.ndim != 2:
        raise ValueError('Expect 2-D input label')

    colormap = create_label_colormap()

    if np.max(label) >= len(colormap):
        raise ValueError('label value too large.')

    return colormap[label]


def vis_segmentation(image, seg_map):
    """Visualizes input image, segmentation map and overlay view."""
    plt.figure(figsize=(20, 4))
    grid_spec = gridspec.GridSpec(1, 4, width_ratios=[6, 6, 6, 1])

    plt.subplot(grid_spec[0])
    plt.imshow(image)
    plt.axis('off')
    plt.title('input image')

    plt.subplot(grid_spec[1])
    seg_image = label_to_color_image(seg_map).astype(np.uint8)
    plt.imshow(seg_image)
    plt.axis('off')
    plt.title('segmentation map')

    plt.subplot(grid_spec[2])
    plt.imshow(image)
    plt.imshow(seg_image, alpha=0.7)
    plt.axis('off')
    plt.title('segmentation overlay')

    unique_labels = np.unique(seg_map)
    ax = plt.subplot(grid_spec[3])
    plt.imshow(FULL_COLOR_MAP[unique_labels].astype(np.uint8), interpolation='nearest')
    ax.yaxis.tick_right()
    plt.yticks(range(len(unique_labels)), LABEL_NAMES[unique_labels])
    plt.xticks([], [])
    ax.tick_params(width=0.0)
    plt.grid('off')
    plt.show()


LABEL_NAMES = np.asarray([
    'road', 'sidewalk', 'building', 'wall', 'fence', 'pole', 'traffic light',
    'traffic sign', 'vegetation', 'terrain', 'sky', 'person', 'rider', 'car', 'truck',
    'bus', 'train', 'motorcycle', 'bicycle', 'void'])

FULL_LABEL_MAP = np.arange(len(LABEL_NAMES)).reshape(len(LABEL_NAMES), 1)
FULL_COLOR_MAP = label_to_color_image(FULL_LABEL_MAP)

"""### Load the model from a frozen graph
There are two model checkpoints pre-trained on Cityscapes with different network backbones: MobileNetV2 and Xception65. We default to use MobileNetV2 for faster inference.
"""

MODEL_NAME = 'mobilenetv2_coco_cityscapes_trainfine'
#MODEL_NAME = 'xception65_cityscapes_trainfine'

_DOWNLOAD_URL_PREFIX = 'http://download.tensorflow.org/models/'
_MODEL_URLS = {
    'mobilenetv2_coco_cityscapes_trainfine':
        'deeplabv3_mnv2_cityscapes_train_2018_02_05.tar.gz',
    'xception65_cityscapes_trainfine':
        'deeplabv3_cityscapes_train_2018_02_06.tar.gz',
}
_TARBALL_NAME = 'deeplab_model.tar.gz'

model_dir = tempfile.mkdtemp()
tf.gfile.MakeDirs(model_dir)

download_path = os.path.join(model_dir, _TARBALL_NAME)
print('downloading model, this might take a while...')
urllib.request.urlretrieve(_DOWNLOAD_URL_PREFIX + _MODEL_URLS[MODEL_NAME], download_path)
print('download completed! loading DeepLab model...')

MODEL = DeepLabModel(download_path)
print('model loaded successfully!')

"""### Run on the sample image
The sample image is frame #0 in the MIT Driving Scene Segmentation (DriveSeg) Dataset.
"""

SAMPLE_IMAGE = 'mit_driveseg_sample.png'
if not os.path.isfile(SAMPLE_IMAGE):
    print('downloading the sample image...')
    SAMPLE_IMAGE = urllib.request.urlretrieve('https://github.com/lexfridman/mit-deep-learning/blob/master/tutorial_driving_scene_segmentation/mit_driveseg_sample.png?raw=true')[0]
print('running deeplab on the sample image...')

def run_visualization(SAMPLE_IMAGE):
    """Inferences DeepLab model and visualizes result."""
    original_im = Image.open(SAMPLE_IMAGE)
    seg_map = MODEL.run(original_im)
    vis_segmentation(original_im, seg_map)

run_visualization(SAMPLE_IMAGE)

def vis_segmentation_stream(image, seg_map, index):
    """Visualizes segmentation overlay view and stream it with IPython display."""
    plt.figure(figsize=(12, 7))

    seg_image = label_to_color_image(seg_map).astype(np.uint8)
    plt.imshow(image)
    plt.imshow(seg_image, alpha=0.7)
    plt.axis('off')
    plt.title('segmentation overlay | frame #%d'%index)
    plt.grid('off')
    plt.tight_layout()

    # Show visualization in a streaming fashion.
    f = BytesIO()
    plt.savefig(f, format='jpeg')
    IPython.display.display(IPython.display.Image(data=f.getvalue()))
    f.close()
    plt.close()


def run_visualization_video(frame, index):
    """Inferences DeepLab model on a video file and stream the visualization."""
    original_im = Image.fromarray(frame[..., ::-1])
    seg_map = MODEL.run(original_im)
    vis_segmentation_stream(original_im, seg_map, index)


SAMPLE_VIDEO = 'mit_driveseg_sample.mp4'
if not os.path.isfile(SAMPLE_VIDEO): 
    print('downloading the sample video...')
    SAMPLE_VIDEO = urllib.request.urlretrieve('https://github.com/lexfridman/mit-deep-learning/raw/master/tutorial_driving_scene_segmentation/mit_driveseg_sample.mp4')[0]
print('running deeplab on the sample video...')

video = cv.VideoCapture(SAMPLE_VIDEO)
# num_frames = 598  # uncomment to use the full sample video
num_frames = 30

try:
    for i in range(num_frames):
        _, frame = video.read()
        if not _: break
        run_visualization_video(frame, i)
        IPython.display.clear_output(wait=True)
except KeyboardInterrupt:
    plt.close()
    print("Stream stopped.")

"""### Evaluation
Now let's evaluate the model performance with the ground truth annotation. First read the annotation from a tar file.
"""

class DriveSeg(object):
    """Class to load MIT DriveSeg Dataset."""

    def __init__(self, tarball_path):
        self.tar_file = tarfile.open(tarball_path)
        self.tar_info = self.tar_file.getmembers()
    
    def fetch(self, index):
        """Get ground truth by index.

        Args:
            index: The frame number.

        Returns:
            gt: Ground truth segmentation map.
        """
        tar_info = self.tar_info[index + 1]  # exclude index 0 which is the parent directory
        file_handle = self.tar_file.extractfile(tar_info)
        gt = np.fromstring(file_handle.read(), np.uint8)
        gt = cv.imdecode(gt, cv.IMREAD_COLOR)
        gt = gt[:, :, 0]  # select a single channel from the 3-channel image
        gt[gt==255] = 19  # void class, does not count for accuracy
        return gt


SAMPLE_GT = 'mit_driveseg_sample_gt.tar.gz'
if not os.path.isfile(SAMPLE_GT): 
    print('downloading the sample ground truth...')
    SAMPLE_GT = urllib.request.urlretrieve('https://github.com/lexfridman/mit-deep-learning/raw/master/tutorial_driving_scene_segmentation/mit_driveseg_sample_gt.tar.gz')[0]

dataset = DriveSeg(SAMPLE_GT)
print('visualizing ground truth annotation on the sample image...')

original_im = Image.open(SAMPLE_IMAGE)
gt = dataset.fetch(0)  # sample image is frame 0
vis_segmentation(original_im, gt)

"""### Evaluate on the sample image
There are many ways to measure the performance of a segmentation model. The most straight forward one is pixel accuracy, which calculates how many pixels are correctly predicted. Another commonly used one is the standard Jaccard Index (intersection-over-union) as IoU = TP ⁄ (TP+FP+FN), where TP, FP, and FN are the numbers of true positive, false positive, and false negative pixels, respectively.
"""

def evaluate_single(seg_map, ground_truth):
    """Evaluate a single frame with the MODEL loaded."""    
    # merge label due to different annotation scheme
    seg_map[np.logical_or(seg_map==14,seg_map==15)] = 13
    seg_map[np.logical_or(seg_map==3,seg_map==4)] = 2
    seg_map[seg_map==12] = 11

    # calculate accuracy on valid area
    acc = np.sum(seg_map[ground_truth!=19]==ground_truth[ground_truth!=19])/np.sum(ground_truth!=19)
    
    # select valid labels for evaluation
    cm = confusion_matrix(ground_truth[ground_truth!=19], seg_map[ground_truth!=19], 
                          labels=np.array([0,1,2,5,6,7,8,9,11,13]))
    intersection = np.diag(cm)
    union = np.sum(cm, 0) + np.sum(cm, 1) - np.diag(cm)
    return acc, intersection, union


print('evaluating on the sample image...')

original_im = Image.open(SAMPLE_IMAGE)
seg_map = MODEL.run(original_im)
gt = dataset.fetch(0)  # sample image is frame 0
acc, intersection, union = evaluate_single(seg_map, gt)
class_iou = np.round(intersection / union, 5)
print('pixel accuracy: %.5f'%acc)
print('mean class IoU:', np.mean(class_iou))
print('class IoU:')
print(tabulate([class_iou], headers=LABEL_NAMES[[0,1,2,5,6,7,8,9,11,13]]))

"""### Evaluate on the sample video"""

print('evaluating on the sample video...', flush=True)

video = cv.VideoCapture(SAMPLE_VIDEO)
# num_frames = 598  # uncomment to use the full sample video
num_frames = 30

acc = []
intersection = []
union = []

for i in tqdm(range(num_frames)):
    _, frame = video.read()
    original_im = Image.fromarray(frame[..., ::-1])
    seg_map = MODEL.run(original_im)
    gt = dataset.fetch(i)
    _acc, _intersection, _union = evaluate_single(seg_map, gt)
    intersection.append(_intersection)
    union.append(_union)
    acc.append(_acc)

class_iou = np.round(np.sum(intersection, 0) / np.sum(union, 0), 4)
print('pixel accuracy: %.4f'%np.mean(acc))
print('mean class IoU: %.4f'%np.mean(class_iou))
print('class IoU:')
print(tabulate([class_iou], headers=LABEL_NAMES[[0,1,2,5,6,7,8,9,11,13]]))

"""### Optional: leverage temporal information
One thing makes video scene segmentation different from image segmentation is the availability of previous frames, which contains valuable temporal information that may help with perception. The open question is how can we use such temporal information. Let's try conbine the prediction of two frames instead of only one frame, making smoother predictions over time.
"""

print('evaluating on the sample video with temporal smoothing...', flush=True)

video = cv.VideoCapture(SAMPLE_VIDEO)
# num_frames = 598  # uncomment to use the full sample video
num_frames = 30

acc = []
intersection = []
union = []
prev_seg_map_logits = 0

for i in tqdm(range(num_frames)):
    _, frame = video.read()
    original_im = Image.fromarray(frame[..., ::-1])
    
    # Get the logits instead of label prediction
    seg_map_logits = MODEL.run(original_im, OUTPUT_TENSOR_NAME='ResizeBilinear_3:0')
    
    # Add previous frame's logits and get the results
    seg_map = np.argmax(seg_map_logits + prev_seg_map_logits, -1)
    prev_seg_map_logits = seg_map_logits
    
    gt = dataset.fetch(i)
    _acc, _intersection, _union = evaluate_single(seg_map, gt)
    intersection.append(_intersection)
    union.append(_union)
    acc.append(_acc)
    
class_iou = np.round(np.sum(intersection, 0) / np.sum(union, 0), 4)
print('pixel accuracy: %.4f'%np.mean(acc))
print('mean class IoU: %.4f'%np.mean(class_iou))
print('class IoU:')
print(tabulate([class_iou], headers=LABEL_NAMES[[0,1,2,5,6,7,8,9,11,13]]))

"""

---


***Special Thanks***

***Professor David J Malan - [CS50x](https://www.linkedin.com/posts/anees-a-5baa4a232_cs50x-india-code4all-activity-6982980019190988800-PGbR?utm_source=share&utm_medium=member_desktop)*** 💻

&&


***MIT-Open course ware [MOOC](https://ocw.mit.edu/)*** 🏫



*Self Taught Engineer*

---

"""