import numpy as np
from fcm import fcmean

recs = 200
data1 = np.random.normal(10, 1, size=(recs, 2))
data2 = np.random.normal(12, 1, size=(recs, 2))
data3 = np.random.normal(14, 1, size=(recs, 2))
data = np.concatenate((data1, data2, data3), axis=0)
# data = data1
number_of_clustes = 3
# data = np.random.normal(20, 20, size=(2, 2))

print(np.shape(data))
# print(data)
centers, res = fcmean(c=number_of_clustes, iter_num=10, data=data)

print("------- Result --------")
print(res)
print(centers)
print(len(centers))
from plots import plot_points

plot_points(data, res, centers)

# for i in range(len(res)):
#     if res[i] != res[0]:
#         print(i)
#         break
