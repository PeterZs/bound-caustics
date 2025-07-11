#  pip install -v figuregen==1.0.1

import os
os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"
import cv2
import simpleimageio as sio
import figuregen
from figuregen.util.templates import *
from figuregen.util.image import Cropbox

def readexr(a, crop = {}):
    imga = cv2.imread(a, cv2.IMREAD_UNCHANGED).astype("float")[:, :, [2, 1, 0]]
    return np.minimum(imga, 1e3) 

figure = CropComparison(
    reference_image=readexr("results/fig_diamond_Ref.exr"),
    method_images=[
        readexr("results/fig_diamond_cs_gamma10.exr"),
        readexr("results/fig_diamond_cs_multiuni.exr"),
        readexr("results/fig_diamond_cs_one.exr"),
        readexr("results/fig_diamond_cs_enum.exr"),
    ],
    crops=[
        Cropbox(top=150, left=960, height=60, width=60, scale=5),
        Cropbox(top=540, left=1400, height=80, width=80, scale=5),
    ],
    scene_name="Diamonds (10 + 4 sec)",
    method_names=["Reference","Ours", "Uniform", "One-sample",  "Enum"]
)
figuregen.figure([figure.figure_row], width_cm=12, filename="results/cmp_sample_diamond.pdf")
os.system("results\\cmp_sample_diamond.pdf")
# Please modify the figuregen template!!!
# @property
# def error_metric_name(self) -> str:
#     return "RelMSE"

# def compute_error(self, reference_image, method_image) -> Tuple[str, List[float]]:
        # return image.relative_mse_outlier_rejection(method_image, reference_image, 0.01, 0.1)
