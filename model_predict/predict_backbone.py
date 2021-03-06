# MIT License
# Copyright (c) 2017  Inc.
# Coded by: scrs



import numpy as np
import scipy.signal
from tqdm import tqdm

import gc

import cv2
import matplotlib.pyplot as plt


def _spline_window(window_size, power=2,  flag_show=False):
    """
    Squared spline (power=2) window function:

    """
    intersection = int(window_size/4)
    wind_outer = (abs(2*(scipy.signal.triang(window_size))) ** power)/2
    wind_outer[intersection:-intersection] = 0

    wind_inner = 1 - (abs(2*(scipy.signal.triang(window_size) - 1)) ** power)/2
    wind_inner[:intersection] = 0
    wind_inner[-intersection:] = 0

    wind = wind_inner + wind_outer
    wind = wind / np.average(wind)

    if flag_show:
        x = len(wind)
        x = list(range(x))
        plt.plot(x, wind, 'k')
        area = sum(wind)
        print("window area = {}".format(area))

    return wind



cached_2d_windows = dict()
def _window_2D(window_size, power=2, flag_show=False):
    """
    Make a 1D window function, then infer and return a 2D window function.
    Done with an augmentation, and self multiplication with its transpose.
    Could be generalized to more dimensions.
    """
    # Memoization
    global cached_2d_windows
    key = "{}_{}".format(window_size, power)
    if key in cached_2d_windows:
        wind = cached_2d_windows[key]
    else:
        wind = _spline_window(window_size, power)
        wind = np.expand_dims(np.expand_dims(wind, 3), 3)
        wind = wind * wind.transpose(1, 0, 2)
        if flag_show:
            # For demo purpose, let's look once at the window:

            plt.imshow(wind[:, :, 0], cmap="gray")
            # plt.title("2D Windowing Function for a Smooth Blending of "
            #           "Overlapping Patches")
            plt.show()
        cached_2d_windows[key] = wind
    return wind

def _pad_img(img, window_size, subdivisions, flag_show=False):
    """
    Add borders to img for a "valid" border pattern according to "window_size" and
    "subdivisions".
    Image is an np array of shape (x, y, nb_channels).
    """
    aug = int(round(window_size * (1 - 1.0/subdivisions)))
    more_borders = ((aug, aug), (aug, aug), (0, 0))
    ret = np.pad(img, pad_width=more_borders, mode='reflect')
    gc.collect()

    if flag_show:
        # For demo purpose, let's look once at the window:
        plt.imshow(ret)
        plt.title("Padded Image for Using Tiled Prediction Patches\n"
                  "(notice the reflection effect on the padded borders)")
        plt.show()
    return ret


def _unpad_img(padded_img, window_size, subdivisions):
    """
    Undo what's done in the `_pad_img` function.
    Image is an np array of shape (x, y, nb_channels).
    """
    aug = int(round(window_size * (1 - 1.0/subdivisions)))
    ret = padded_img[
        aug:-aug,
        aug:-aug,
        :
    ]
    gc.collect()
    return ret

def _rotate_mirror_do(im,slices=1):
    """
    Duplicate an np array (image) of shape (x, y, nb_channels) 8 times, in order
    to have all the possible rotations and mirrors of that image that fits the
    possible 90 degrees rotations.

    It is the D_4 (D4) Dihedral group:
    https://en.wikipedia.org/wiki/Dihedral_group
    """

    mirrs = []
    if slices==1:
        mirrs.append(np.array(im))
    elif slices==2:
        mirrs.append(np.array(im))
        mirrs.append(np.rot90(np.array(im), k=1))
    elif slices==4:
        mirrs.append(np.array(im))
        mirrs.append(np.rot90(np.array(im), k=1))
        im = np.array(im)[:, ::-1]
        mirrs.append(np.array(im))
        mirrs.append(np.rot90(np.array(im), k=1))
    else:
        mirrs.append(np.array(im))
        mirrs.append(np.rot90(np.array(im), k=1))
        mirrs.append(np.rot90(np.array(im), k=2))
        mirrs.append(np.rot90(np.array(im), k=3))
        im = np.array(im)[:, ::-1]
        mirrs.append(np.array(im))
        mirrs.append(np.rot90(np.array(im), k=1))
        mirrs.append(np.rot90(np.array(im), k=2))
        mirrs.append(np.rot90(np.array(im), k=3))

    return mirrs


def _rotate_mirror_undo(im_mirrs, slices=1):
    """
    merges a list of 8 np arrays (images) of shape (x, y, nb_channels) generated
    from the `_rotate_mirror_do` function. Each images might have changed and
    merging them implies to rotated them back in order and average things out.

    It is the D_4 (D4) Dihedral group:
    """
    sum = np.array(im_mirrs[0])
    if slices == 1:
        pass
    elif slices == 2:
        sum += np.rot90(np.array(im_mirrs[1]), k=3)
    elif slices == 4:
        sum += np.rot90(np.array(im_mirrs[1]), k=3)
        sum += np.array(im_mirrs[2])[:, ::-1]
        sum += np.rot90(np.array(im_mirrs[3]), k=3)[:, ::-1]
    else:
        sum += np.rot90(np.array(im_mirrs[1]), k=3)
        sum += np.rot90(np.array(im_mirrs[2]), k=2)
        sum += np.rot90(np.array(im_mirrs[3]), k=1)
        sum += np.array(im_mirrs[4])[:, ::-1]
        sum += np.rot90(np.array(im_mirrs[5]), k=3)[:, ::-1]
        sum += np.rot90(np.array(im_mirrs[6]), k=2)[:, ::-1]
        sum += np.rot90(np.array(im_mirrs[7]), k=1)[:, ::-1]

    """test: output each result of mirros"""
    # n = 0
    # for one_img in origs:
    #     cv2.imwrite('./data/predict/pre_smooth_unrotate' + str(n + 1) + '.png', one_img[128:-128, 128:-128])
    #     n +=1

    # return np.mean(origs, axis=0)
    out_back = sum/slices
    return out_back


def _windowed_subdivs(padded_img, window_size, subdivisions, nb_classes, pred_func):
    """
    Create tiled overlapping patches.

    Returns:
        5D numpy array of shape = (
            nb_patches_along_X,
            nb_patches_along_Y,
            patches_resolution_along_X,
            patches_resolution_along_Y,
            nb_output_channels
        )

    Note:
        patches_resolution_along_X == patches_resolution_along_Y == window_size
    """
    WINDOW_SPLINE_2D = _window_2D(window_size=window_size, power=2)

    step = int(window_size/subdivisions)
    padx_len = padded_img.shape[0]
    pady_len = padded_img.shape[1]
    subdivs = []

    for i in range(0, padx_len-window_size+1, step):
        subdivs.append([])
        for j in range(0, pady_len-window_size+1, step): # here padx_len should be pady_len
            patch = padded_img[i:i+window_size, j:j+window_size, :]
            subdivs[-1].append(patch)

    # Here, `gc.collect()` clears RAM between operations.
    # It should run faster if they are removed, if enough memory is available.
    gc.collect()
    subdivs = np.array(subdivs)
    gc.collect()
    a, b, c, d, e = subdivs.shape
    subdivs = subdivs.reshape(a * b, c, d, e)
    gc.collect()

    subdivs = pred_func(subdivs)
    gc.collect()
    subdivs = subdivs.astype(np.float16)
    subdivs = np.array([patch * WINDOW_SPLINE_2D for patch in subdivs])
    gc.collect()

    # Such 5D array:
    subdivs = subdivs.reshape(a, b, c, d, nb_classes)
    gc.collect()

    # convert to uint8
    subdivs = subdivs.astype("uint8")

    return subdivs


def _recreate_from_subdivs(subdivs, window_size, subdivisions, padded_out_shape):
    """
    Merge tiled overlapping patches smoothly.
    """
    step = int(window_size/subdivisions)
    padx_len = padded_out_shape[0]
    pady_len = padded_out_shape[1]

    y = np.zeros(padded_out_shape)

    a = 0
    for i in range(0, padx_len-window_size+1, step):
        b = 0
        for j in range(0, pady_len-window_size+1, step):
            windowed_patch = subdivs[a, b]
            y[i:i+window_size, j:j+window_size] = y[i:i+window_size, j:j+window_size] + windowed_patch
            b += 1
        a += 1
    return y / (subdivisions ** 2)


def _windowed_subdivs_multiclassbands(padded_img, model, window_size, subdivisions, real_classes, pred_func):
    """
    Create tiled overlapping patches.

    Returns:
        5D numpy array of shape = (
            nb_patches_along_X,
            nb_patches_along_Y,
            patches_resolution_along_X,
            patches_resolution_along_Y,
            nb_output_channels
        )

    Note:
        patches_resolution_along_X == patches_resolution_along_Y == window_size
    """
    WINDOW_SPLINE_2D = _window_2D(window_size=window_size, power=2)

    step = int(window_size/subdivisions)
    padx_len = padded_img.shape[0]
    pady_len = padded_img.shape[1]
    subdivs = []

    for i in range(0, padx_len-window_size+1, step):
        subdivs.append([])
        for j in range(0, pady_len-window_size+1, step): # here padx_len should be pady_len
            patch = padded_img[i:i+window_size, j:j+window_size, :]
            subdivs[-1].append(patch)

    # Here, `gc.collect()` clears RAM between operations.
    # It should run faster if they are removed, if enough memory is available.
    gc.collect()
    subdivs = np.array(subdivs)
    gc.collect()
    a, b, c, d, e = subdivs.shape
    subdivs = subdivs.reshape(a * b, c, d, e)
    gc.collect()

    subdivs = pred_func(subdivs, model, real_classes)
    gc.collect()
    subdivs = subdivs.astype(np.float16)
    subdivs = np.array([patch * WINDOW_SPLINE_2D for patch in subdivs])
    gc.collect()

    # Such 5D array:
    subdivs = subdivs.reshape(a, b, c, d, real_classes)
    gc.collect()

    # convert to uint8
    # subdivs = subdivs.astype("uint8")

    return subdivs


def predict_img_with_smooth_windowing_multiclassbands(input_img, model, window_size, subdivisions, real_classes, pred_func, PLOT_PROGRESS = True):
    """
    Apply the `pred_func` function to square patches of the image, and overlap
    the predictions to merge them smoothly.

    :return :real_class channels, range[0,255] corresponding to [0,1] probabilities
    """

    pad = _pad_img(input_img, window_size, subdivisions)
    pads = _rotate_mirror_do(pad)

    # Note that the implementation could be more memory-efficient by merging
    # the behavior of `_windowed_subdivs` and `_recreate_from_subdivs` into
    # one loop doing in-place assignments to the new image matrix, rather than
    # using a temporary 5D array.

    # It would also be possible to allow different (and impure) window functions
    # that might not tile well. Adding their weighting to another matrix could
    # be done to later normalize the predictions correctly by dividing the whole
    # reconstructed thing by this matrix of weightings - to normalize things
    # back from an impure windowing function that would have badly weighted
    # windows.

    # For example, since the U-net of Kaggle's DSTL satellite imagery feature
    # prediction challenge's 3rd place winners use a different window size for
    # the input and output of the neural net's patches predictions, it would be
    # possible to fake a full-size window which would in fact just have a narrow
    # non-zero dommain. This may require to augment the `subdivisions` argument
    # to 4 rather than 2.

    res = []
    for pad in tqdm(pads):
        # For every rotation:
        # predict each rotation with smooth window
        sd = _windowed_subdivs_multiclassbands(pad, model, window_size, subdivisions, real_classes, pred_func)

        # Merge tiled overlapping patches smoothly.
        one_padded_result = _recreate_from_subdivs(
            sd, window_size, subdivisions,
            padded_out_shape=list(pad.shape[:-1])+[real_classes])

        res.append(one_padded_result)
        del sd, pad,one_padded_result
        gc.collect()


    # Merge after rotations:
    del pads
    gc.collect()

    padded_results = _rotate_mirror_undo(res)

    # padded_results = _rotate_mirror_undo_by_vote(res, 5)

    prd = _unpad_img(padded_results, window_size, subdivisions)

    prd = prd[:input_img.shape[0], :input_img.shape[1], :]

    """
    save [0,1] probabilities to [0,255]
    """
    prd = prd * 255.0

    if PLOT_PROGRESS:
        for idx in range(real_classes):
            plt.imshow(prd[:,:,idx])
            plt.title("Smoothly Merged Patches that were Tiled Tighter")
            plt.show()

    return prd  # probabilities for each target: [0,255]
