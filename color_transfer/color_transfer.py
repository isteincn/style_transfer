from skimage import color
from scipy.linalg import fractional_matrix_power as fractional_power
from numpy.linalg import matrix_power
import cv2
from .commonfunctions import *


# does color transfer through converting an image to the LAB color space, changing
# the mean and variance there, then converting the image back into RGB
def color_transfer_lab(content, style):
    # convert images to LAB space
    style_lab = cv2.cvtColor(style.astype("float32"), cv2.COLOR_RGB2LAB).astype("float32")  # color.rgb2lab(style)
    content_lab = cv2.cvtColor(content.astype("float32"), cv2.COLOR_RGB2LAB).astype("float32")  # color.rgb2lab(content)
    # calculate mean
    content_mu = np.mean(content_lab, axis=tuple(range(2)))
    style_mu = np.mean(style_lab, axis=tuple(range(2)))
    # calculate standard deviation
    content_std = np.std(content_lab, axis=tuple(range(2)))
    style_std = np.std(style_lab, axis=tuple(range(2)))
    # transfer
    content_lab = (content_lab - content_mu) * (content_std / style_std) + style_mu
    content_lab = np.clip(content_lab, 0, 255)
    # convert back to RGB
    content_rgb = cv2.cvtColor(content_lab, cv2.COLOR_LAB2RGB)  # color.lab2rgb(content_lab)
    return content_rgb


# doe color transfer through histogram matching
def color_transfer_hm(content, style):
    original = content.copy()
    # calculate the mean
    content_mu = np.mean(content, axis=(0, 1))
    style_mu = np.mean(content, axis=(0, 1))
    # print(style.reshape(-1, 3).shape)
    # calculate the covariance
    style_cov = np.cov(style.reshape(-1, 3).T)
    content_cov = np.cov(content.reshape(-1, 3).T)
    # get A, b
    A = fractional_power(style_cov, 0.5).dot(fractional_power(content_cov, -0.5))
    b = (style_mu.T - A.dot(content_mu.T)).T
    x, y, z = np.shape(content)
    content = np.dot(A, original.reshape(-1, z).T)
    content = (content.T + b).reshape(x, y, z)
    return content
