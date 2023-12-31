import matplotlib.pyplot as plt
import numpy as np

def plot_in_out_histogram(hist_name, id_list_name, id_list, out_list_name, out_list):
    print("start plot_in_out_histogram")
    print(f"{id_list_name}: {id_list}")
    print(f"{id_list_name} type: {type(id_list)}")
    print(f"{id_list_name} shape: {id_list.shape}")
    print(f"{out_list_name}: {out_list}")
    print(f"{out_list_name} shape: {out_list.shape}")
    # Plot histograms
    plt.hist(id_list, bins=100, alpha=0.5, color='blue', label=id_list_name)
    plt.hist(out_list, bins=100, alpha=0.5, color='orange', label=out_list_name)

    # Add labels and title
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.title(f'Histogram of ID VS OUT {hist_name}')

    # Add legend
    plt.legend()

    # Show the plot
    plt.savefig('result.png')
    # plt.show()
    print("finish plot_in_out_histogram")

plot_in_out_histogram("ood", "cifar10", np.random.rand(200), "cifar100", np.random.rand(200) + 5)
