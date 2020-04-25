
import numpy as np
import MotionClouds as mc
import os

N_Y = 256
#downscale = 1
#fx, fy, ft = mc.get_grids(mc.N_X/downscale, mc.N_Y/downscale, mc.N_frame/downscale)
fx, fy, ft = mc.get_grids(N_Y, N_Y, 256)
#fx, fy, ft = mc.get_grids(512, 512, 256)

timetag = '2017-09-25-1700_balaV1' # TODO : use that date instead

name = '2014-12-10_balaV1'
vext = '.png'
mc.figpath = '.'
try:
    os.mkdir(os.path.join(mc.figpath, name))
except:
    pass

# Experimental constants 
contrast = 1.
N_frame_total = 25
# Clouds parameters in absolute units
#N_X = fx.shape[0]
width = 29.7*N_Y/1050
phi_sf_0 = 3. # Optimal spatial frequency [cpd]

sf_0 = phi_sf_0*width/N_Y
B_sf = sf_0   # BW spatial frequency
B_V = .7     # BW temporal frequency (speed plane thickness)
theta = 0.0   # Central orientation

# generate zip files
dry_run = True
dry_run = False

for B_theta in [0, np.pi/32, np.pi/16, np.pi/8, np.pi/4, np.pi/2, np.inf]:
    for seed in [42, 1973, 2015]:
        name_ = name + '_B_theta_' + str(B_theta).replace('.', '_')
        name_ += '_seed_' + str(seed)
        if not dry_run:
            if  not(os.path.isfile(os.path.join(mc.figpath, name, name_ + vext))):
                mc_i = mc.envelope_gabor(fx, fy, ft, 
                                         V_X=0., V_Y=0., B_V=B_V, 
                                         sf_0=sf_0, B_sf=B_sf, 
                                         theta=0., B_theta=B_theta)
                im = mc.random_cloud(mc_i)[:, :, :N_frame_total]
                mc.anim_save(mc.rectif(im, contrast=contrast), os.path.join(mc.figpath, name, name_), vext=vext)
            else:
                print(' MC ' + os.path.join(mc.figpath, name, name_) + ' already done')
        else:
            print(' MC ' + os.path.join(mc.figpath, name, name_) + ' skipped  (dry run)')
