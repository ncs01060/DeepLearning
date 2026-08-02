# def step_function(x):
#     if x > 0:
#         return 1
#     else:
#         return 0
import numpy as np
def step_function(x):
    y = x > 0
    return y.astype(int)

print(step_function(np.array([-1.0,1.0,2.0])))