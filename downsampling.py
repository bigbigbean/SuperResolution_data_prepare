import numpy as np
from skimage.transform import resize
from skimage.measure import block_reduce
import nibabel as nib
import SimpleITK as sitk
#
# '''
# Downsamples a 3D-image along the z-axis.
# '''
# def downsample_z_axis(img, downsampling_factor=2):
#     return block_reduce(img, block_size=(1,1,downsampling_factor), func=np.max)

# '''
# Interpolation Method chosen for the project.
# '''
# def spline_interpolation(img, HR_shape, interp_order):
#     return resize(img, output_shape=HR_shape, mode='symmetric', order=interp_order)

# Downsamples a 3D-image along the z-axis.
mri_path = "t1-thin.nii.gz"
mri_down_path = "t1-thin-down5.nii.gz"
mri_array0 = nib.load(mri_path)
mri_image = sitk.ReadImage(mri_path)
print(mri_image.GetSpacing())
mri_array = mri_array0.get_data()
affine = mri_array0.affine
mri_down_array = block_reduce(mri_array,block_size=(1,1,5),func=np.max)

mri_down = nib.Nifti1Image(mri_down_array,affine)
nib.save(mri_down,mri_down_path)
mri_down_image = sitk.ReadImage(mri_down_path)
mri_down_image.SetSpacing([0.9375,0.9375,3])
print(mri_down_image.GetSpacing())
sitk.WriteImage(mri_down_image,mri_down_path)

