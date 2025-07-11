TESTID = "fig_plane"
import sys 
sys.path.append("..") 
from labcommon import *
groups = {
    # "cs_enum": "-Dspp=1 -Dforce_gamma=1e9 -Ddistr_max=10 ",
    "cs_one": "-Dspp=64 -Dforce_sample=1 -Dforce_gamma=0 ",
    # "cs_var": "-Dspp=8 -Dspec_var=0.00001 -Ddistr_max=10 ",
    # "cs_mul": "-Dspp=10 -Dforce_sample=64 -Ddistr_max=10 ",
    # "cs_gamma10": "-Dspp=14 -Dforce_gamma=500 -Ddistr_max=100 ",
    # "cs_gamma1000": "-Dspp=4 -Dforce_gamma=1000 -Ddistr_max=1 ",
    # "cs_multiuni": "-Dspp=16 -Dforce_gamma=40000 -Ddistr_max=0.000001 ",
}
for test_name0, gparam in groups.items():
    print(test_name0)
    exr_filename0 = "results/%s_%s.exr " % (TESTID, test_name0)
    cmd = "..\\..\\mts1\\cbuild\\bin\\mitsuba.exe "
    cmd += "plane_pcp.xml "
    cmd += "-DuseResultant=false -DmethodMask=0 -DdistrPath=../../results/sample_map.txt "
    cmd += "-o %s " % exr_filename0
    cmd += gparam
    t = my_run_cmd(TESTID, cmd, test_name0, instant=True)
    print("%.3f" % t)