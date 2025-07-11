```
p0 = np.array([1, 2.0, -2])
p30 = np.array([-3, 0.0, -3])
p31 = np.array([6, 0.000001, 0])
p32 = np.array([0, 0.000002, 6])
pD0, pD1, pD2 = p30, p31, p32
mesh = read_obj("../data/slab10k.obj", [0.0, 0.0, 0])
ground = np.array([p30, p30+p31, p30+p32])

constraint_file_name = "constraints.txt"

def normalize(x):
    return x / norm(x)

def array(a):
    return np.array(a)

RES = 128
N_THREAD = 16
JACOBIAN_COMPRESS = 1   # 0-accurate 1-compressed   accurate is almost for one bounce only

CHAIN_TYPE = 22 # 1 for reflection and 2 for refraction
CHAIN_LENGTH = 1 if CHAIN_TYPE < 10 else 2

η_VAL = 0.6666666666666666
SHADING_NORMAL = True # the first bounce (close to light)
SHADING_NORMAL2 = True # the second bounce (close to receiver)

# CORE HYPERPARAMETERS
AR = 1e1 # approx ratio
Am = 1e-3 # minimum irradiance
AM = 1e2 # maximum irradiance
INF_AREA_TOL = 1e-3
u1TOLERATE = 0.1
U1T = 0.3

# SOME PARAMETERS THAT MAY SPEED UP THE ALGORITHM
MAX_SUBDIV = 256  # not strictly enforced when the positional denom contains zero

# NOT IMPORTANT PARAMETERS
β_STRONG_THRES = 1e9
β_MIN = 1e-9
SPLAT_SUBDIV_THRES = 1e-3

BATCH_SIZE = 64
```