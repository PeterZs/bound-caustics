TESTID = "fig_slab"
import sys 
sys.path.append("..") 
from labcommon import *

groups = {
    "cs_enum": "-Dspp=1 -Dforce_gamma=1e9 ",
    "cs_one": "-Dspp=20 -Dforce_sample=1 ",
    "cs_gamma100": "-Dspp=2 -Dforce_gamma=70 ",
    "cs_multiuni": "-Dspp=2 -Dforce_gamma=5000 -Ddistr_max=0.0001 ",
    # "cs_gamma10": "-Dspp=1 -Dforce_gamma=10 ",
    # "cs_gamma1": "-Dspp=1 -Dforce_gamma=1 ",
    # "cs_opt_sv": "-Dspp=1 -Dspec_var=0.001 -Duse_max_var=true ",
    # "cs_opt_pv": "-Dspp=1 -Dspec_var=1 -Duse_max_var=false ",
}

for test_name0, gparam in groups.items():
    print(test_name0)
    exr_filename0 = "results/%s_%s.exr " % (TESTID, test_name0)
    cmd = "..\\..\\mts1\\cbuild\\bin\\mitsuba.exe "
    cmd += "slab_pcp.xml "
    cmd += "-DuseResultant=false -DmethodMask=0 -DdistrPath=../../results/sample_map.txt "
    cmd += "-o %s " % exr_filename0
    cmd += "-p 16 "
    cmd += gparam
    t = my_run_cmd(TESTID, cmd, test_name0, instant=False)
    print("%.3f" % t)