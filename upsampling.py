import numpy as np
from skimage.transform import resize
import nibabel as nib
import SimpleITK as sitk
import scipy

# '''
# Interpolation Method chosen for the project.
# '''
# def spline_interpolation(img, HR_shape, interp_order):
#     return resize(img, output_shape=HR_shape, mode='symmetric', order=interp_order)


# Interpolation Method chosen for the project.
mri_path = "t1-thin.nii.gz"
mri_down_path = "t1-thin-down5.nii.gz"
mri_up_path = "t1-thin-down5-up5-1.nii.gz"
mri_thin_image = sitk.ReadImage(mri_path)
mri_down_array0 = nib.load(mri_down_path)
mri_down_array = mri_down_array0.get_data()
affine = mri_down_array0.affine

# mri_up_array = resize(mri_down_array,(384,276,104),order=3,mode='symmetric')
# mri_up = nib.Nifti1Image(mri_up_array,affine)
# nib.save(mri_up,mri_up_path)
# mri_up_image = sitk.ReadImage(mri_up_path)
# mri_up_image.SetSpacing(mri_thin_image.GetSpacing())
# print(mri_up_image.GetSpacing())
# sitk.WriteImage(mri_up_image,mri_up_path)

# def resample_volume(img, spacing_old, spacing_new, bounds=None):
#     (z_axis, y_axis, x_axis) = np.shape(img)
#     print('img: {} old spacing: {} new spacing: {}'.format(np.shape(img), spacing_old, spacing_new))
#     resize_factor = np.array(spacing_old) / spacing_new
#     new_shape = np.round(np.shape(img) * resize_factor)
#     real_resize_factor = new_shape / np.shape(img)
#     img_rescaled = scipy.ndimage.interpolation.zoom(img, real_resize_factor, mode='nearest').astype(np.int16)
#     img_array_normalized = copy_normalized(img_rescaled)
#     img_tmp = img_array_normalized.copy()
#     # determine what the mean will be on the anticipated value range
#     mu, var = 0., 0.
#     if bounds is not None:
#         min_bound, max_bound = bounds
#         img_tmp = truncate(img_tmp, min_bound, max_bound)
#         mu = np.mean(img_tmp)
#         var = np.var(img_tmp)
#     return img_array_normalized

# mri_up_array = resample_volume(mri_down_array,spacing_old =[0.9375,0.9375,3],spacing_new=[0.9375,0.9375,3])
# mri_up_array = resample_volume(mri_down_array,spacing_old =[0.9375,0.9375,3],spacing_new=mri_thin_image.GetSpacing())
spacing_old =[0.9375,0.9375,3]
spacing_new = mri_thin_image.GetSpacing()
resize_factor = np.array(spacing_old) / spacing_new
new_shape = np.round(np.shape(mri_down_array) * resize_factor)
real_resize_factor = new_shape / np.shape(mri_down_array)
mri_up_array = scipy.ndimage.interpolation.zoom(mri_down_array, real_resize_factor, mode='nearest').astype(np.int16)

mri_up = nib.Nifti1Image(mri_up_array,affine)
nib.save(mri_up,mri_up_path)
mri_up_image = sitk.ReadImage(mri_up_path)
mri_up_image.SetSpacing(mri_thin_image.GetSpacing())
print(mri_up_image.GetSpacing())
sitk.WriteImage(mri_up_image,mri_up_path)