import pandas as pd
import matplotlib.pyplot as plt
import os

# Method to remove coloumns by list of names
def remove_cols(df, cols_to_drop):

    df = df.drop(columns=cols_to_drop, inplace=False)

    return df

# Method to save the plot to the directory
def save_fig(f_name, dir_name):
    plt.figure(f_name)
    plt.savefig(os.path.join(dir_name, "_".join( f_name.split() ) + ".png"), transparent=True)
    plt.close()