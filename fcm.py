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
        # print(memberships)
        for j in range(c):
            # print("m", np.shape(memberships[:,j]))
            uikpowm = [pow(u, m) for u in memberships[:, j]]
            # print("uikpowm", np.shape(uikpowm))
            sorat = [uikpowm[i] * data[i] for i in range(row_num)]
            # print("sorat", np.shape(sorat))
            # print("sorat", sorat)
            # print("sorat[0]", sorat[0])
            # print("inside zigma sum", np.sum(uikpowm))
            # print("inside zigma ", uikpowm)
            for i in range(feature_num):
                centers[j][i] = np.sum([sorat[k][i] / np.sum(uikpowm) for k in range(row_num)])
        # print("new centers", centers)
    ## TODO : Return Value must be a list (array) containing cluster centers

    return centers, [np.argmax(memberships[i]) for i in range(row_num)]
