import numpy as np


def generate_data(mean, var, size): 
    data = np.random.normal(mean, var**0.5, size)
    return data


def calc_stats(data): 
    mean = np.mean(data)
    median = np.median(data)
    std_dev = np.std(data)
    print("Mean:", mean, "Median:", median, "Standard Deviation:", std_dev)


import matplotlib.pyplot as plt


def plot_data(data): 
    plt.hist(data, bins=30)
    plt.show()


def main():
    data = generate_data(180, 25, 1000)
    calc_stats(data)
    plot_data(data)


main()
