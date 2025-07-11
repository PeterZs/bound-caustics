RES = 512
N_THREAD = 16
JACOBIAN_COMPRESS = 1   # 0-accurate 1-compressed   accurate is almost for one bounce only

CHAIN_TYPE = 22 # 1 for reflection and 2 for refraction
CHAIN_LENGTH = 1 if CHAIN_TYPE < 10 else 2

η_VAL = 0.6666666666666666
SHADING_NORMAL = False # the first bounce (close to light)
SHADING_NORMAL2 = False # the second bounce (close to receiver)

# CORE HYPERPARAMETERS
INF_AREA_TOL = SPLAT_SUBDIV_THRES = 1e-4
U1T = u1TOLERATE = 0.125001
AR = 1e1 # approx ratio

# NOT IMPORTANT PARAMETERS
Am = 1e-5 # minimum irradiance
AM = 1e2 # maximum irradiance
β_STRONG_THRES = 1e99  # please fix explicit before run this code
β_MIN = 1e-9

BATCH_SIZE = 64