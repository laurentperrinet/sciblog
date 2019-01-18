#!/usr/bin/env python3
# -*- coding: utf-8 -*
import numpy as np
import MotionClouds as mc
import os

viewingDistance = 30 # cm
screen_height_cm = 29 # cm
#un deg / cm
print('visual angle of the screen', 2*np.arctan(screen_height_cm/2/viewingDistance)*180/np.pi, ' degrees')
print('degrees per centimeter', 2*np.arctan(screen_height_cm/2/viewingDistance)*180/np.pi/screen_height_cm)

screen_height_px = 1024 # pixels 
#screen_height_px = 256 # pixels 
deg_per_px = 2*np.arctan(screen_height_cm/2/viewingDistance)*180/np.pi/screen_height_px
print('degrees per pixel', deg_per_px)

fps = 60 # frames per second
T = 1 # duration of one period in second

mc.N_X, mc.N_Y, mc.N_frame = screen_height_px, screen_height_px, int(fps*T)

print('width of these motion clouds (', mc.N_X, ', ', mc.N_Y, ')')
print('width of stimulus in degrees', mc.N_X * deg_per_px)
phi_sf_0 = .06 # Optimal spatial frequency [cpd]
print('Optimal spatial frequency in cycles per degree', phi_sf_0)
print('Optimal spatial frequency in cycles per window = ', phi_sf_0 *  mc.N_X * deg_per_px)
sf_0 = phi_sf_0 * deg_per_px
print('cycles per pixel = ', sf_0)

# Experimental constants 
contrast = 1.
B_sf = 0.1*sf_0 # 0.1   # BW spat. freq.
B_ft = .1 # BW temp. freq.

B_V = B_ft/sf_0     # BW in speed ("plane thickness")
print('B_V = ', B_V)
theta = 0.0   # Central orientation
# generate all files
dry_run = True
dry_run = False

#downscale = 1
fx, fy, ft = mc.get_grids(mc.N_X, mc.N_Y, mc.N_frame)

name = '2017-04-19_biphoton'
vext = '.png'
mc.figpath = '.'
try:
    os.mkdir(os.path.join(mc.figpath, name))
except:
    pass
print('-'*50)
print('Starting protocol')
print('-'*50)
for B_theta in [0, np.pi/32, np.pi/16, np.pi/8, np.pi/4, np.pi/2, np.inf]:
    if B_theta == np.inf: B_theta_str = 'inf'
    else: B_theta_str = str(int(np.ceil(B_theta*180/np.pi)))
    for seed in [42, 1973, 2015]:
        name_ = name + '_B_theta_' + B_theta_str
        name_ += '_seed_' + str(seed)
        print('Cooking:', name_)
        if not dry_run:
            if  not(os.path.isfile(os.path.join(mc.figpath, name, name_ + vext))):
                mc_i = mc.envelope_gabor(fx, fy, ft, 
                                         V_X=0., V_Y=0., B_V=B_V, 
                                         sf_0=sf_0, B_sf=B_sf, 
                                         theta=0., B_theta=B_theta)
                im = mc.random_cloud(mc_i)
                im = mc.rectif(im, contrast=contrast, verbose=True)
                # TERRIBLE HACK !
                im[0, 0, :] = 0.
                im[-1, -1, :] = 1.
                mc.anim_save(im, os.path.join(mc.figpath, name, name_), T_movie=T, vext=vext)
            else:
                print(' MC ' + os.path.join(mc.figpath, name, name_) + ' already done')
        else:
            print(' MC ' + os.path.join(mc.figpath, name, name_) + ' skipped  (dry run)')
