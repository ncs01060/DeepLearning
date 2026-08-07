import numpy as np

def softmax(a):
        c = np.max(a)
        exp_a = np.exp(a - c) # 오버플로우 대책
        sum_exp_a = np.sum(exp_a)
        y = exp_a / sum_exp_a
        return y

def cross_entropy_error(y,t):
    delta = 1e-7
    return -np.sum(t * np.log(y+delta))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))