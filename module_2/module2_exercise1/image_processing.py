# Download image
import matplotlib
import os
import matplotlib.image as mpimg
import gdown
import numpy as np

file_id = '1i9dqan21DjQoG5Q_VEvm0LrVwAlXD0vB'
path = '/Users/nguyendung/git/AIO_exercises/module_2/module2_exercise1/'
gdown.download(
    f'https://drive.google.com/uc?id={file_id}', output=f'{path}', quiet=False)
img_down = os.path.join(path, 'dog.jpeg')

img = mpimg.imread(img_down)


def convert_grey_lightness(vector):
    return ((np.max(vector) + np.min(vector))/2)


def convert_grey_average(vector):
    return (np.sum(vector)/len(vector))


def convert_grey_luminosity(vector):
    return (vector[0] * 0.21 + vector[1]*0.72 + vector[2]*0.07)


# Q12
gray_img_01 = np.apply_along_axis(
    convert_grey_lightness, axis=2, arr=img)  # Your Code Here
print(gray_img_01[0, 0])

# Q13
gray_img_02 = np.apply_along_axis(
    convert_grey_average, axis=2, arr=img)  # Your Code Here
print(gray_img_02[0, 0])

# Q14
gray_img_03 = np.apply_along_axis(
    convert_grey_luminosity, axis=2, arr=img)  # Your Code Here
print(gray_img_03[0, 0])
