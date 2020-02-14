import numpy as np
import matplotlib.pyplot as plt



def bernoulli_trial(n, p):
    '''Returns Bernoulli schema and number of successes'''
    n_success = 0
    trial = list()
    for i in range(n):
        rand = np.random.random()
        if rand > p:
            trial.append(0)
        else:
            trial.append(1)
            n_success += 1
    return trial, n_success

def main():
    print(bernoulli_trial(10, 0.4))
    np.random.seed(42)
    print(bernoulli_trial(10, 0.4))
    print(bernoulli_trial(10, 0.4))
    list_n_success = list()
    for i in range(100000):
        trial_list, n_success = bernoulli_trial(10, 0.4)
        # print(trial_list, n_success)
        list_n_success.append(n_success)
    plot_bernoulli(list_n_success)
    ecdf(list_n_success)
    plt.show()

def plot_bernoulli(list_n_success):
    plt.hist(list_n_success)
    plt.show()

def ecdf(list_n_success):
    x = sorted(list_n_success)
    y = np.arange(1, len(list_n_success) + 1)
    plt.plot(x, y, marker='.', linestyle='none')
    # plt.title('Accumulated Bernoulli')

main()