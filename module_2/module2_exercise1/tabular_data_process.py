# Download image
import pandas as pd
import matplotlib
import os
import matplotlib.image as mpimg
import gdown
import numpy as np
import pandas

file_id = '1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq'
path = '/Users/nguyendung/git/AIO_exercises/module_2/module2_exercise1/'
gdown.download(
    f'https://drive.google.com/uc?id={file_id}', output=f'{path}', quiet=False)

df = pd.read_csv(f'{path}/advertising.csv')
sale_data = df['Sales'].to_numpy()

# Q15
max_index = np.argmax(sale_data)
print(f'Max: {sale_data[max_index]} - Index: {max_index}')
# Q16
tv_data = df['TV'].to_numpy()
print(f'average on TV column: {np.average(tv_data)}')
# Q17
greater_than_20_in_sale = sale_data[sale_data >= 20]
print(f'number of sales having avlue greater than 20 : {
      len(greater_than_20_in_sale)}')
# Q18
radio_data = df['Radio'].to_numpy()
radio_having_sale_greater_than15 = radio_data[sale_data >= 15]
print(f'average value of radio having sale greater or equal 15: {
      np.average(radio_having_sale_greater_than15)}')
# Q19
newspaper_data = df['Newspaper'].to_numpy()
average_newspaper = np.average(newspaper_data)
sale_having_newspaper_greater_than_average_newspaper = sale_data[
    newspaper_data > average_newspaper]
print(f'sum of sale having newspaper values greater than its average value:{
      np.sum(sale_having_newspaper_greater_than_average_newspaper)}')
# Q20
average_sale = np.average(sale_data)
score = np.where(sale_data > average_sale, 'Good', np.where(
    sale_data < average_sale, 'Bad', 'Average'))
print(score[7:10])
# Q21
distance_to_average = np.abs(sale_data - average_sale)
distance_to_average_ = np.where(
    distance_to_average == average_sale, 10000, distance_to_average)
min_distance_to_sale = np.argmin(distance_to_average_)
closest_to_sale = sale_data[min_distance_to_sale]
score_2 = np.where(sale_data > closest_to_sale, 'Good', np.where(
    sale_data < closest_to_sale, 'Bad', 'Average'))
print('average_sale', average_sale)
print('closest_to_sale', closest_to_sale)
print(score_2[7:10])
