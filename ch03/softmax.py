import numpy as np
class SoftMax:
    def __init__(self):
        pass
    def softmax(self,a):
        c = np.max(a)
        exp_a = np.exp(a - c) # 오버플로우 대책
        sum_exp_a = np.sum(exp_a)
        y = exp_a / sum_exp_a
        return y

a = np.array([0.3,2.9,4.0])
y = SoftMax()
y = y.softmax(a)
print(y) # 확률
print(np.sum(y)) 