import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()


(x_train, t_train), (x_test,t_test) = load_mnist(flatten=True,normalize=False)

# 각 데이터의 형상 출력
# print(x_train.shape)
# print(t_train.shape)
# print(x_test.shape)
# print(t_test.shape)

img = x_train[0]
label = t_train[0]
print(label)

print(img.shape) # 1차원으로 저장되어있음
img = img.reshape(28,28) # 우리가 보기 위해 28x28크기로 변형
print(img.shape)

img_show(img)