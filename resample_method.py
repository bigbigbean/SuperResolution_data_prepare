import scipy
import numpy as np

# from xianglei
# img是nib load的image array,spacing_old是原来的spacing，spacing_new是新的spacing
def resample_volume(img, spacing_old, spacing_new, bounds=None):
    (z_axis, y_axis, x_axis) = np.shape(img)
    print('img: {} old spacing: {} new spacing: {}'.format(np.shape(img), spacing_old, spacing_new))
    resize_factor = np.array(spacing_old) / spacing_new
    new_shape = np.round(np.shape(img) * resize_factor)
    real_resize_factor = new_shape / np.shape(img)
    img_rescaled = scipy.ndimage.interpolation.zoom(img, real_resize_factor, mode='nearest').astype(np.int16)
    img_array_normalized = copy_normalized(img_rescaled)
    img_tmp = img_array_normalized.copy()
    # determine what the mean will be on the anticipated value range
    mu, var = 0., 0.
    if bounds is not None:
        min_bound, max_bound = bounds
        img_tmp = truncate(img_tmp, min_bound, max_bound)
        mu = np.mean(img_tmp)
        var = np.var(img_tmp)
    return img_array_normalized
