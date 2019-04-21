import numpy as np
import random

m = 2
epsilon = 2.22045e-16


def fcmean(c, iter_num, data):
    row_num = len(data)
    feature_num = len(data[0])
    memberships = np.zeros(shape=(row_num, c))
    centers = np.zeros(shape=(c, feature_num))
    random_records = random.sample(range(row_num), c)
    print(random_records)
    for i in range(c):
        centers[i] = data[random_records[i]]
    for i in range(iter_num):
        print("--------- iteration", i, "---------")
        D = np.zeros(shape=(row_num, c))
        for j in range(c):
            for k in range(row_num):
                D[k][j] = np.sum(pow((np.multiply((data[k] - centers[j]), (data[k] - centers[j]))), (1 / (m - 1))))
        for j in range(c):
            for k in range(row_num):
                memberships[k][j] = (1 / (D[k][j] + epsilon)) / np.sum([(1 / (d + epsilon)) for d in D[k]])
        print(memberships)
        for j in range(c):
            # print("m", np.shape(memberships[:,j]))
            inside_zigma = [pow(u, m) for u in memberships[:, j]]
            # print("inside_zigma", np.shape(inside_zigma))
            sorat = np.matmul(inside_zigma, data)
            # print("sorat", np.shape(sorat))
            centers[j] = np.sum(sorat) / np.sum(inside_zigma)

    return [np.argmax(memberships[i]) for i in range(row_num)]
