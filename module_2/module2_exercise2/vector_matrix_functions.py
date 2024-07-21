
import cv2
import numpy as np


def compute_vector_length(vector):
    print('np.dot(vector,vector', np.dot(vector, vector))
    len_of_vector_w1 = np.sqrt(np.dot(vector, vector))
    # len_of_vector_w2 = np.linalg.norm(vector)
    return len_of_vector_w1


def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result


def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix, vector)
    return result


def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result


def inverse_matrix(matrix):
    result = np.linalg.inv(matrix)
    return result


def compute_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors


def compute_cosine(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    cos_sim = dot_product / (norm_v1 * norm_v2)
    return cos_sim


def compute_difference(bg_img, input_img):
    difference_single_channel = input_img - bg_img
    return difference_single_channel


def compute_binary_mask(difference_single_channel):
    difference_binary = np.where(difference_single_channel == 0, 0, 255)
    return difference_binary


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(
        bg1_image,
        ob_image
    )

    binary_mask = compute_binary_mask(difference_single_channel)

    output = np. where(binary_mask == 255, ob_image, bg2_image)

    return output


# Q1
vector = np.array([-2, 4, 9, 21])
result = compute_vector_length(vector)
print(round(result, 2))

# Q2:
v1 = np. array([0, 1, -1, 2])
v2 = np. array([2, 5, 1, 0])
result = compute_dot_product(v1, v2)
print(round(result, 2))

# Q3:
x = np. array([[1, 2],
               [3, 4]])
k = np. array([1, 2])
print('result \n', x.dot(k))

# Q4:
x = np. array([[-1, 2],
               [3, -4]])
k = np. array([1, 2])
print('result \n', x@k)

# Q5:
m = np. array([[-1, 1, 1], [0, -4, 9]])
v = np. array([0, 2, 1])
result = matrix_multi_vector(m, v)
print(result)

# Q6:
m1 = np. array([[0, 1, 2], [2, -3, 1]])
m2 = np. array([[1, -3], [6, 1], [0, -1]])
result = matrix_multi_matrix(m1, m2)
print(result)

# Q7:
m1 = np.eye(3)  # creates a 3x3 identity matrix
m2 = np. array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
result = m1@m2
print(result)

# Q8:
m1 = np.eye(2)
m1 = np. reshape(m1, (-1, 4))[0]
m2 = np. array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1@m2
print(result)

# Q9:
m1 = np. array([[1, 2], [3, 4]])
m1 = np. reshape(m1, (-1, 4), "F")[0]
m2 = np. array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]])
result = m1@m2
print(result)

# Q10:
m1 = np. array([[-2, 6], [8, -4]])
result = inverse_matrix(m1)
print(result)

# Q11:
matrix = np. array([[0.9, 0.2], [0.1, 0.8]])
eigenvalues, eigenvectors = compute_eigenvalues_eigenvectors(matrix)
print(eigenvectors)

# Q12:
x = np. array([1, 2, 3, 4])
y = np. array([1, 0, 3, 0])
result = compute_cosine(x, y)
print(round(result, 3))

bg1_image = cv2.imread('./pic_data/GreenBackground.png', 1)
bg1_image = cv2.resize(bg1_image, (678, 381))
bg1_image = bg1_image.astype(np.float32)

ob_image = cv2.imread('./pic_data/Object.png', 1)
ob_image = cv2.resize(ob_image, (678, 381))
ob_image = ob_image.astype(np.float32)

bg2_image = cv2.imread('./pic_data/NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image, (678, 381))
bg2_image = bg2_image.astype(np.float64)

difference_single_channel = compute_difference(bg1_image, ob_image)
difference_single_channel_save = difference_single_channel.astype(np.uint8)
cv2.imwrite('./pic_data/difference_image.png', difference_single_channel_save)

binary_mask = compute_binary_mask(difference_single_channel)
binary_mask_save = binary_mask.astype(np.uint8)
cv2.imwrite('./pic_data/binary_mask.png', binary_mask_save)

new_image = replace_background(bg1_image, bg2_image, ob_image)
new_image_save = new_image.astype(np.uint8)
cv2.imwrite('./pic_data/new_image.png', new_image_save)
