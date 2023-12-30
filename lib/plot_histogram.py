import matplotlib.pyplot as plt
import numpy as np
import torch

def plot_in_out_histogram(hist_name, id_list_name, id_list, out_list_name, out_list):
    # Plot histograms
    plt.hist(id_list, bins=30, alpha=0.5, color='blue', label=id_list_name.cpu().detach().numpy())
    plt.hist(out_list, bins=30, alpha=0.5, color='orange', label=out_list_name.cpu().detach().numpy())

    # Add labels and title
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of ID VS OUT {hist_name}')

    # Add legend
    plt.legend()

    # Show the plot
    plt.show()
