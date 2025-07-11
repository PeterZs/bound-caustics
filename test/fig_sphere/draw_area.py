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
    return np.minimum(imga, 1) 

figure = CropComparison(
    reference_image=readexr("results/fig_plane_Ref1.exr"),
    method_images=[
        readexr("results/fig_plane_Bounded1.exr"),
        readexr("results/fig_plane_Enum1.exr"),
        readexr("results/fig_plane_PT.exr"),
        readexr("results/fig_plane_LT.exr"),
        readexr("results/fig_plane_PPG.exr"),
        readexr("results/fig_plane_MEMLT.exr"),
    ],
    crops=[
        Cropbox(top=288, left=1026, height=80, width=80, scale=5),
        Cropbox(top=330, left=880, height=80, width=80, scale=5),
    ],
    scene_name="Plane Area (30 sec)",
    method_names=["Reference", "Ours",  "SP", "PT", "LT", "PPG", "MEMLT"],
    spp_list= [10, 1, 2, 2, 82, 300]
)
figuregen.figure([figure.figure_row], width_cm=17, filename="results/fig_plane1.pdf")
os.system("results\\fig_plane1.pdf")
# Please modify the figuregen template!!!
# @property
# def error_metric_name(self) -> str:
#     return "RelMSE"

# def compute_error(self, reference_image, method_image) -> Tuple[str, List[float]]:
        # return image.relative_mse_outlier_rejection(method_image, reference_image, 0.01, 0.1)
