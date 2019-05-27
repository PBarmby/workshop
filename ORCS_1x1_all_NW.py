#!/usr/bin/env python 

##### SN3 #####
from orcs.process import SpectralCube      
from orb.core import HDFCube, OutHDFQuadCube
import numpy as np

cube = SpectralCube('/data/sitelle/orb/17BQ06/17BF17/M33-NW_SN3.merged.cm1.1.0.hdf5')

axis, sky = cube.extract_spectrum(1866,963,50)
sky = sky/(3.14159*50*50)
outcube = OutHDFQuadCube('/data/sitelle/orb/17BQ06/17BF17/M33-W_SN3.merged.cm1.1.0_modif.hdf5', cube.shape, cube.config.QUAD_NB)

cube = HDFCube('/data/sitelle/orb/17BQ06/17BF17/M33-NW_SN3.merged.cm1.1.0.hdf5')

for iquad in range(cube.config.QUAD_NB):

    xmin,xmax,ymin,ymax=cube.get_quadrant_dims(iquad)
    iquad_data = cube.get_data(xmin,xmax,ymin,ymax,0,cube.dimz)
    for i in range(0,cube.dimz):
	iquad_data[:,:,i] = iquad_data[:,:,i] - sky[i]
    iquad_data[(np.isfinite(iquad_data) == False)]= 1e-22 # Modifs
    iquad_data[(iquad_data < -1e-16)]= -1e-22 # Modifs
    iquad_data[(iquad_data > 1e-9)]= 1e-22 # Modifs

    outcube.write_quad(iquad,data=iquad_data)


deep_frame = np.zeros([2048,2064])
cube2 = cube.get_all_data()

for i in range(0,cube.dimz):

    deep_frame = deep_frame + cube2[:,:,i]

deep_frame[(np.isfinite(deep_frame) == False)] = 1e-22
deep_frame[(deep_frame < 0 )] = 1e-22

outcube.append_deep_frame(deep_frame)
outcube.append_header(cube.get_cube_header())
outcube.append_calibration_laser_map(cube.get_calibration_laser_map())

outcube.close()


cube = SpectralCube('/data/sitelle/orb/17BQ06/17BF17/M33-W_SN3.merged.cm1.1.0_modif.hdf5')

for i in range(25,2075,50):
   with open("/data/sitelle/orb/17BQ08/17BF17/M33-SE/M33-SE_5.reg", "r+") as f:
       old = f.read() # read everything in the file
       f.seek(0) # rewind
       f.write(old[0:193]+'\n'+"box("+str(i)+",1032,50,2044,0)")

   cube.fit_lines_in_region('/data/sitelle/orb/17BQ08/17BF17/M33-SE/M33-SE_5.reg',
                         ('Halpha', '[NII]6548', '[NII]6583','[SII]6716','[SII]6731'),
                         fmodel='sinc',
                         pos_def=['1','2','2','2','2'],
                         pos_cov = [-160,-160],
			 snr_guess=None,amp_def=['1', '2', '2','3','4'],
                         amp_guess=[1,1,2.96784195554,1,1], 
			 binning=1, max_iter=2000, nofilter=True)

#### SN2 #####

cube = SpectralCube('/data/sitelle/orb/17BQ06/17BF17/M33-NW_SN2.merged.cm1.1.0.hdf5')

axis, sky = cube.extract_spectrum(1866,963,50)
sky = sky/(3.14159*50*50)
outcube = OutHDFQuadCube('/data/sitelle/orb/17BQ06/17BF17/M33-W_SN2.merged.cm1.1.0_modif.hdf5', cube.shape, cube.config.QUAD_NB)

cube = HDFCube('/data/sitelle/orb/17BQ06/17BF17/M33-NW_SN2.merged.cm1.1.0.hdf5')

for iquad in range(cube.config.QUAD_NB):

    xmin,xmax,ymin,ymax=cube.get_quadrant_dims(iquad)
    iquad_data = cube.get_data(xmin,xmax,ymin,ymax,0,cube.dimz)
    for i in range(0,cube.dimz):
        iquad_data[:,:,i] = iquad_data[:,:,i] - sky[i]
    iquad_data[(np.isfinite(iquad_data) == False)]= 1e-22 # Modifs
    iquad_data[(iquad_data < -1e-16)]= -1e-22 # Modifs
    iquad_data[(iquad_data > 1e-9)]= 1e-22 # Modifs

    outcube.write_quad(iquad,data=iquad_data)


deep_frame = np.zeros([2048,2064])
cube2 = cube.get_all_data()

for i in range(0,cube.dimz):

    deep_frame = deep_frame + cube2[:,:,i]

deep_frame[(np.isfinite(deep_frame) == False)] = 1e-22
deep_frame[(deep_frame < 0 )] = 1e-22

outcube.append_deep_frame(deep_frame)
outcube.append_header(cube.get_cube_header())
outcube.append_calibration_laser_map(cube.get_calibration_laser_map())

outcube.close()

cube = SpectralCube('/data/sitelle/orb/17BQ06/17BF17/M33-W_SN2.merged.cm1.1.0_modif.hdf5')

for i in range(25,2075,50):
   with open("/data/sitelle/orb/17BQ08/17BF17/M33-SE/M33-SE_55.reg", "r+") as f:
       old = f.read() # read everything in the file
       f.seek(0) # rewind
       f.write(old[0:193]+'\n'+"box("+str(i)+",1032,50,2044,0)")

   cube.fit_lines_in_region('/data/sitelle/orb/17BQ08/17BF17/M33-SE/M33-SE_55.reg',
                         ('Hbeta', '[OIII]4959', '[OIII]5007'),
                         fmodel='sinc',
                         pos_def=['1','2','2'],
                         pos_cov = [-160,-160],
                         snr_guess=None,amp_def=['1', '2', '2'],
                         amp_guess=[1,1,3.01],
                         binning=1, max_iter=2000, nofilter=True)


##### SN1 ######

cube = SpectralCube('/data/sitelle/orb/17BQ06/17BF17/M33-NW_SN1.merged.cm1.1.0.hdf5')

axis, sky = cube.extract_spectrum(1866,963,50)
sky = sky/(3.14159*50*50)
outcube = OutHDFQuadCube('/data/sitelle/orb/17BQ06/17BF17/M33-W_SN1.merged.cm1.1.0_modif.hdf5', cube.shape, cube.config.QUAD_NB)

cube = HDFCube('/data/sitelle/orb/17BQ06/17BF17/M33-NW_SN1.merged.cm1.1.0.hdf5')

for iquad in range(cube.config.QUAD_NB):

    xmin,xmax,ymin,ymax=cube.get_quadrant_dims(iquad)
    iquad_data = cube.get_data(xmin,xmax,ymin,ymax,0,cube.dimz)
    for i in range(0,cube.dimz):
        iquad_data[:,:,i] = iquad_data[:,:,i] - sky[i]
    iquad_data[(np.isfinite(iquad_data) == False)]= 1e-22 # Modifs
    iquad_data[(iquad_data < -1e-16)]= -1e-22 # Modifs
    iquad_data[(iquad_data > 1e-9)]= 1e-22 # Modifs

    outcube.write_quad(iquad,data=iquad_data)


deep_frame = np.zeros([2048,2064])
cube2 = cube.get_all_data()

for i in range(0,cube.dimz):

    deep_frame = deep_frame + cube2[:,:,i]

deep_frame[(np.isfinite(deep_frame) == False)] = 1e-22
deep_frame[(deep_frame < 0 )] = 1e-22

outcube.append_deep_frame(deep_frame)
outcube.append_header(cube.get_cube_header())
outcube.append_calibration_laser_map(cube.get_calibration_laser_map())


outcube.close()


cube = SpectralCube('/data/sitelle/orb/17BQ06/17BF17/M33-NW_SN1.merged.cm1.1.0_modif.hdf5')

for i in range(25,2075,50):
   with open("/data/sitelle/orb/17BQ08/17BF17/M33-SE/M33-SE_555.reg", "r+") as f:
       old = f.read() # read everything in the file
       f.seek(0) # rewind
       f.write(old[0:193]+'\n'+"box("+str(i)+",1032,50,2044,0)")

   cube.fit_lines_in_region('/data/sitelle/orb/17BQ08/17BF17/M33-SE/M33-SE_555.reg',
                         [10000000/372.7],
                         fmodel='sinc',
                         pos_def=['1'],
                         pos_cov = [-120],
                         snr_guess=None,amp_def=['1'],
                         #amp_guess=[1],
                         binning=1, max_iter=2000, nofilter=True)

