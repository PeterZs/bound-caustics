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
    imga = np.nan_to_num(imga)
    return np.minimum(imga, 1e1) 

figure = CropComparison(
    reference_image=readexr("results/fig_pool_Ref.exr"),
    method_images=[
        readexr("results/fig_pool_Bounded.exr"),
        readexr("results/fig_pool_Enum.exr"),
        readexr("results/fig_pool_MPG.exr"),
        readexr("results/fig_pool_SMS.exr"),
        readexr("results/fig_pool_UPSMCMC.exr"),
        readexr("results/fig_pool_SPPM.exr"),
    ],
    crops=[
        # Cropbox(top=402, left=654, height=80, width=80, scale=5),
        Cropbox(top=180, left=672, height=80, width=80, scale=5),
    ],
    scene_name="Pool (3 sec)",
    method_names=["Reference", "Ours",  "SP", "MPG", "SMS", "UPSMCMC", "SPPM"],
    spp_list= [2, 1, 5, 8, 3, 15]
)
figuregen.figure([figure.figure_row], width_cm=22, filename="results/fig_pool.pdf")
os.system("results\\fig_pool.pdf")
# Please modify the figuregen template!!!
# @property
# def error_metric_name(self) -> str:
#     return "RelMSE"

# def compute_error(self, reference_image, method_image) -> Tuple[str, List[float]]:
        # return image.relative_mse_outlier_rejection(method_image, reference_image, 0.01, 0.1)
