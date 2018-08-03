import numpy as np
from skimage.transform import resize
import nibabel as nib
import SimpleITK as sitk

# '''
# Interpolation Method chosen for the project.
# '''
# def spline_interpolation(img, HR_shape, interp_order):
#     return resize(img, output_shape=HR_shape, mode='symmetric', order=interp_order)


# Interpolation Method chosen for the project.
mri_path = "t1-thin.nii.gz"
mri_down_path = "t1-thin-down5.nii.gz"
mri_up_path = "t1-thin-down5-up5.nii.gz"
mri_thin_image = sitk.ReadImage(mri_path)
mri_down_array0 = nib.load(mri_down_path)
mri_down_array = mri_down_array0.get_data()
affine = mri_down_array0.affine

mri_up_array = resize(mri_down_array,(384,276,104),order=3,mode='symmetric')
mri_up = nib.Nifti1Image(mri_up_array,affine)
nib.save(mri_up,mri_up_path)
mri_up_image = sitk.ReadImage(mri_up_path)
mri_up_image.SetSpacing(mri_thin_image.GetSpacing())
print(mri_up_image.GetSpacing())
sitk.WriteImage(mri_up_image,mri_up_path)