TESTID = "fig_plane"
import sys

sys.path.append("..")
from labcommon import *

test_name0 = "Bounded1"
exr_filename0 = "results/%s_%s.exr " % (TESTID, test_name0)
cmd = "..\\..\\mts1\\cbuild\\bin\\mitsuba.exe "
cmd += "plane_pcp.xml "
cmd += "-DuseResultant=true -DmethodMask=0 "
cmd += "-DdistrPath=../../results/sample_map.txt "
# cmd += "-DdistrPath=../../data/plane130k.obj "
cmd += "-o %s " % exr_filename0
cmd += "-Dspp=10 "
# t = my_run_cmd(TESTID, cmd, test_name0, instant=True)
# print(t)
# quit()
test_name0 = "Enum1"
exr_filename0 = "results/%s_%s.exr " % (TESTID, test_name0)
cmd = "..\\..\\mts1\\cbuild\\bin\\mitsuba.exe "
cmd += "plane_pcp.xml "
cmd += "-DuseResultant=true -DmethodMask=0 "
cmd += "-o %s " % exr_filename0
cmd += "-Dspp=1 "
# t = my_run_cmd(TESTID, cmd, test_name0, instant=True)
# print(t)
# quit()

test_name2 = "SMS1"
mitsuba2_cmd = "..\\..\\mts\\build\\dist\\mitsuba.exe -m scalar_rgb "
exr_filename2 = "results/%s_%s.exr " % (TESTID, test_name2)
cmd = mitsuba2_cmd
cmd += "plane_mpg.xml "
cmd += "-o %s " % exr_filename2
cmd += f"-Dtimeout=30 "
cmd += f"-Dtrain_auto=false "

# t = my_run_cmd(TESTID, cmd, test_name2, instant=False)
# print(t)

test_name2 = "MPG1"
mitsuba2_cmd = "..\\..\\mts\\build\\dist\\mitsuba.exe -m scalar_rgb "
exr_filename2 = "results/%s_%s.exr " % (TESTID, test_name2)
cmd = mitsuba2_cmd
cmd += "plane_mpg.xml "
cmd += "-o %s " % exr_filename2
cmd += f"-Dtimeout=30 -Dselective=true "
cmd += f"-Dtrain_auto=true "

# t = my_run_cmd(TESTID, cmd, test_name2, instant=True)
# print(t)
# quit()


for tname, iname, spp in [
    # ("PPG", "guided_path_m17", 9999),
    # ("PT", "path", 1000),
    # ("LT", "ptracer", 3000),
    ("MEMLT", "mlt", 280)
]:
    test_name0 = tname
    exr_filename0 = "results/%s_%s.exr " % (TESTID, test_name0)
    cmd = "..\\..\\mts1\\cbuild\\bin\\mitsuba.exe "
    cmd += "plane_pcp.xml "
    cmd += "-o %s " % exr_filename0
    cmd += "-Dintegrator=%s " % iname
    cmd += "-Dtimeout=30 "
    cmd += "-Dspp=%d " % spp
    print(cmd)
    t = my_run_cmd(TESTID, cmd, test_name0, instant=False)
    print(t)
quit()


test_name1 = "Ref1"
exr_filename1 = "results/%s_%s.exr " % (TESTID, test_name1)
cmd = "..\\..\\mts1\\cbuild\\bin\\mitsuba.exe "
cmd += "plane_pcp.xml "
cmd += "-DuseResultant=true -DmethodMask=0 "
cmd += "-o %s " % exr_filename1
cmd += "-Dintegrator=%s " % "sppm"
cmd += "-Dspp=2048 "
cmd += "-DinitialRadius=0.005 "
# t = my_run_cmd(TESTID, cmd, test_name1, instant=True)
# print(t)
