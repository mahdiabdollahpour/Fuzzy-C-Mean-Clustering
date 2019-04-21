import numpy as np
from fcm import fcmean

data1 = np.random.normal(3, 1, size=(1000, 2))
data2 = np.random.normal(100, 1, size=(1000, 2))
data = np.concatenate((data1, data2), axis=0)

# data = np.random.normal(10, 1, size=(2, 2))

print(np.shape(data))
res = fcmean(c=2, iter_num=3, data=data)

print("------- Result --------")
print(res)
