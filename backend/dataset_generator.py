import matplotlib.pyplot as plt
import numpy as np
# generate related variables
from numpy import mean
from numpy import std
from numpy.random import randn
from numpy.random import seed
from sklearn.datasets import make_classification
from sklearn.datasets import make_blobs
from sklearn.datasets import make_gaussian_quantiles

cluster_numbers = [2,3]

plt.figure()
def export_data_to_csv(filename, X, Y):
    #export data to csv
    X_Y = []
    for i in range(len(X)):
        X_Y.append([X[i], Y[i]])
    
    np.savetxt(filename + ".csv", np.asarray(X_Y), delimiter=",", header="x,y")
    
    
def gen_clusters(n_data=4000,n_clus=2, centers=None, point_share="equal", point_dist = "gaussian", add_outliers=False):
    """Generates clusters of data points.

    Args:
        n_data (int, optional): Number of data points. Defaults to 4000.
        n_clus (int, optional): Number of clusters. Defaults to 2.
        centers (list(list(int)), optional): Cluster centers in a list of 2-d points. If not specified, centers will be generated randomly. Defaults to None.
        point_share (list(float), optional): The proportion of all data points assignerd to each cluster. Options: "equal", "skewed".  Defaults to "equal".
        point_dist (str, optional): The distribution of points w.r.t to the center of the cluster. Options: "uniform", "gaussian". Defaults to "gaussian".
        add_outliers (bool, optional): Add outliers between cluster. Defaults to False.
    """
    plt.subplot(325)
    plt.title(" blobs", fontsize="small")
    X1, Y1 = make_blobs(n_samples=[1500, 2500], n_features=2, cluster_std=
                    4.5, centers=[[0,0],[40,40]])
    if(add_outliers):
        X2, Y2 = make_blobs(n_samples=[14,40,25,10], centers=([15,20],[25,20],[20,15],[20,25]), n_features=2, cluster_std=10.0)
        X1 = np.concatenate([X1, X2])
        Y1 = np.concatenate([Y1, Y2])
    plt.scatter(X1[:, 0], X1[:, 1], marker="o", c=Y1, s=25, edgecolor="k")
    export_data_to_csv("clusters_2", X1[:, 0], X1[:, 1])


def gen_correlation(sample_size=4000,slope=100, intercept=50):
    
    plt.subplot(326)
    # seed random number generator
    seed(1)
    # prepare data
    data1 = 20 * randn(sample_size) + 100
    data2 = data1 + (slope * randn(sample_size) + intercept)
    # summarize
    print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
    print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))
    # plot
    plt.scatter(data1, data2)
    export_data_to_csv("correlation_linear", data1, data2)
    

def gen_exponential(sample_size=4000,scale=2):
    
    plt.subplot(323)
    # seed random number generator
    seed(1)
    # prepare data
    data1 = 30 * randn(sample_size)
    data2 = scale * np.power(1.02, data1) + np.random.normal(0, 0.08, sample_size)
    # summarize
    print('data1: mean=%.3f stdv=%.3f' % (mean(data1), std(data1)))
    print('data2: mean=%.3f stdv=%.3f' % (mean(data2), std(data2)))
    # plot
    plt.scatter(data1, data2)
    export_data_to_csv("correlation_exponential", data1, data2)


# def gen_normal_distribution(numPoints=4000):
#     #generate a normal distribution 
#     plt.subplot(121)
#     mu, sigma = 100, 5 # mean and standard deviation
#     s = np.random.normal(mu, sigma, numPoints)

# def gen_bimodal_distribution(numPoints=4000):
#     #generate a bimodal distribution 
#     plt.subplot(122)
#     mu, sigma = 100, 5
#     mu2, sigma2 = 10, 40
#     X1 = np.random.normal(mu, sigma, numPoints)
#     X2 = np.random.normal(mu2, sigma2, numPoints)
#     X = np.concatenate([X1, X2])
#     plt.scatter(X)


gen_correlation(slope = 10, intercept = 50)
gen_clusters(n=4, add_outliers=True)
gen_exponential(scale=0.2)
# gen_normal_distribution(4000)
# gen_bimodal_distribution(4000)

plt.show()