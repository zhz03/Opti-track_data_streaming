import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    position = np.load('data/pos_2021-07-14-02_37_40.npy')

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    for i in range(len(position)):
        ax.scatter(position[i][0], position[i][1], position[i][2])
        
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()