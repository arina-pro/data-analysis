import numpy as np
import matplotlib.pyplot as plt
from bernoulli import ecdf



def ecdf_poisson(lam_list, size):
    poisson_list = list()
    for lam in lam_list:
        ecdf(np.random.poisson(lam=lam, size=size))
    plt.show()



def compare_poisson(n, p):
    sample_binom = np.random.binomial(n, p, size=10000)
    sample_poisson = np.random.poisson(lam=n * p, size=10000)
    ecdf(sample_binom)
    ecdf(sample_poisson)
    plt.show()



def main():
    lam_list = [10, 15, 100]
    ecdf_poisson(lam_list, 10000)
    compare_poisson(10, 0.1)



main()