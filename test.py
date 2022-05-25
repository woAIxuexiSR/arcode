import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from SerializedData import *



if __name__ == "__main__":
    
    filename = "TrainData/gx_10.json"

    d = SerializedData(filename)

    for i in range(20):
        localGaze = d.fetch(i, "localGaze")
        headPos = d.fetch(i, "headPos")
        gazePos = d.fetch(i, "gazePos")
        time = d.fetch(i, "time")
        target = d.fetch(i, "target")

        print(localGaze.shape, headPos.shape, gazePos.shape, time.shape)

        plt.plot(time, headPos[:, 0], c='r')
        plt.plot(time, gazePos[:, 0], c="g")
        plt.plot(time, np.ones_like(time) * target[0], c="b")
        plt.show()