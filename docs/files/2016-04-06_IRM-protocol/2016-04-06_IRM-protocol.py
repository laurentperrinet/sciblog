import numpy as np
import MotionClouds as mc
import os

#downscale = 1
#fx, fy, ft = mc.get_grids(mc.N_X//downscale, mc.N_Y//downscale, mc.N_frame//downscale)
fx, fy, ft = mc.get_grids(512, 512, 128)

name = '2016-04-06_IRM-protocol'
vext = '.png'
mc.figpath = '.'
if not(os.path.isdir(mc.figpath)): os.mkdir(mc.figpath)

# Experimental constants 
contrast = 1.
# Clouds parameters in absolute units
N_X = fx.shape[0]
width = 29.7*256/1050
phi_sf_0 = 2. # Optimal spatial frequency [cpd]

sf_0 = phi_sf_0*width/N_X
B_sf = sf_0   # BW spatial frequency
B_V = .5     # BW temporal frequency (speed plane thickness) WARNING temporal autocorrelation depends on N_frame

# generate zip files
dry_run = True
dry_run = False

def make_one_block(seed, B_theta, N_sub, B_V=B_V, N_frame_sub=6, N_theta=12):
    np.random.seed(seed)
    N_X, N_Y, N_frame = fx.shape
    im = np.zeros((N_X, N_Y, 0))
    disk = mc.frequency_radius(fx, fy, ft) < .5

    for i_sub in range(N_sub):
        theta = np.int(np.random.rand()*N_theta) * np.pi / N_theta
        mc_i = mc.envelope_gabor(fx, fy, ft, 
                                         V_X=0., V_Y=0., B_V=B_V, 
                                         sf_0=sf_0, B_sf=B_sf, 
                                         theta=theta, B_theta=B_theta)
        im = np.concatenate((im, (mc.rectif(mc.random_cloud(mc_i))*disk + .5*(1-disk))[:, :, :N_frame_sub]), axis=-1)
    return im
                
#for i_B_theta, B_theta in enumerate([np.pi/24, np.pi/12, np.pi/6, np.pi/3, np.pi][::-1]):
for i_B_theta, B_theta in enumerate([np.pi/12, np.inf][::-1]):
    if B_theta == np.inf: B_theta_str = 'inf'
    else: B_theta_str = str(int(np.ceil(B_theta*180/np.pi)))
    for seed in [2016 + i for i in range(7)]:
        name_ = name + '_B_theta_' + B_theta_str
        name_ += '_seed_' + str(seed)
        if not dry_run:
            if  not(os.path.isfile(os.path.join(mc.figpath, name, name_ + vext))):
                im = make_one_block(seed=seed+i_B_theta, B_theta=B_theta, N_sub=20, N_frame_sub=6, N_theta=12)
                mc.anim_save(mc.rectif(im, contrast=contrast), os.path.join(mc.figpath, name, name_), vext=vext)
            else:
                print(' MC ' + os.path.join(mc.figpath, name, name_) + ' already done')
        else:
            print(' MC ' + os.path.join(mc.figpath, name, name_) + ' skipped  (dry run)')
