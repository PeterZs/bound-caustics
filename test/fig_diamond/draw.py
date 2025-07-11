import os
os.environ["OPENCV_IO_ENABLE_OPENEXR"]="1"
import cv2
import simpleimageio as sio
# import figuregen
# from figuregen.util.templates import *
# from figuregen.util.image import Cropbox
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from myfiguregen.util.templates import *
from myfiguregen.util.image import Cropbox

def readexr(a, crop = {}):
    imga = cv2.imread(a, cv2.IMREAD_UNCHANGED).astype("float")[:, :, [2, 1, 0]]
    return np.minimum(imga, 1e4) * 1.5

figure = CropComparison(
    reference_image=readexr("results/fig_diamond_Ref.exr"),
    method_images=[
        readexr("results/fig_diamond_Bounded.exr"),
        readexr("results/fig_diamond_BoundedSMSU.exr"),
        readexr("results/fig_diamond_MPG.exr"),
        readexr("results/fig_diamond_SMS.exr"),
        readexr("results/fig_diamond_Uniform.exr"),
        readexr("results/fig_diamond_UPSMCMC.exr"),
        readexr("results/fig_diamond_SPPM.exr"),
    ],
    crops=[
        Cropbox(top=500, left=1370, height=100, width=100, scale=5),
        Cropbox(top=660, left=400, height=100, width=100, scale=5),
    ],
    scene_name="Diamonds (50 sec)",
    method_names=["Reference", "Ours+Det", "Ours+Stoc", "MPG", "SMS",  "Path Cuts*", "UPSMCMC", "SPPM"],
    spp_list= [32, 28, 11, 9, 12, 27, 204]
)
figuregen.figure([figure.figure_row], width_cm=22, filename="results/fig_diamond.pdf")
os.system("results\\fig_diamond.pdf")
# Please modify the figuregen template!!!
# @property
# def error_metric_name(self) -> str:
#     return "RelMSE"

# def compute_error(self, reference_image, method_image) -> Tuple[str, List[float]]:
        # return image.relative_mse_outlier_rejection(method_image, reference_image, 0.01, 0.1)
