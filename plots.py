import matplotlib.pyplot as plt


def plot_points(data, res, centers):
    g0_d0 = [data[i][0] for i in range(len(res)) if res[i] == 0]
    g0_d1 = [data[i][1] for i in range(len(res)) if res[i] == 0]

    g1_d0 = [data[i][0] for i in range(len(res)) if res[i] == 1]
    g1_d1 = [data[i][1] for i in range(len(res)) if res[i] == 1]

    g2_d0 = [data[i][0] for i in range(len(res)) if res[i] == 2]
    g2_d1 = [data[i][1] for i in range(len(res)) if res[i] == 2]

    plt.plot(g0_d0, g0_d1, 'ro', g1_d0, g1_d1, 'yo', g2_d0, g2_d1, 'go')
    for i in range(len(centers)):
        plt.plot(centers[i][0],centers[i][1],'b^',markersize=20)
    plt.show()
