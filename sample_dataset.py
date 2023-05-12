import os
import csv

import pandas as pd


def read_data(input_file, max_num):
    """
    Load data into pandas DataFrame format.
    """
    
    df_data = pd.read_csv(input_file, index_col=None, header=0)
    # find all records belong to the desired type
    df_data = df_data[df_data['bias_type']==b_type]
    fraction  = len(df_data)
    df_data = df_data.groupby('stereo_antistereo').apply(lambda x: x.sample(frac=fraction))
    df_data = df_data[:max_num]

    return df_data

b_type = 'gender'
max_num = 80
input_file = './data/crows_pairs_anonymized.csv'
output_file = './data/crows_pairs_sampled_'+ b_type+'.csv'
df_data = read_data(input_file, max_num)
df_data.head(10)
df_data.to_csv(output_file)