import numpy as np
# 나쁜 예시 - 수치 미분

def numerical_diff(f,x):
    h = 1e-50
    return (f(x+h) - f(x)) / h 

