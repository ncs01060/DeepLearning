import numpy as np
x = np.array([1.0,2.0,3.0])
# print(x)
# print(type(x))
y = np.array([2.0,4.0,6.0])
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x / 2.0) << 스칼라 값으로 나누기

# # 행렬
# A = np.array([[1,2],[3,4]])
# # print(A)
# B = np.array([[3,0],[0,6]])
# # print(A+B)
# # print(A*B)

# A = np.array([[1,2],[3,4]])
# B = np.array([10,20])
# print(A*B)

X = np.array([[51,55],[14,19],[0,4]])
X = X.flatten() # X를 1차원 배열로 변환(평탄화)
print(X)
print(X[np.array([0,2,4])])
print(X>15)
print(X[X>15])