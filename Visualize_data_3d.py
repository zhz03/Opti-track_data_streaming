import numpy as np
import matplotlib.pyplot as plt

def get_xyz(position):
    position10 = []
    position11 = []
    position12 = []
    for i in range(len(position)):
        position10.append(position[i][0])
        position11.append(position[i][1])
        position12.append(position[i][2])
    
    return position10,position11,position12

if __name__ == '__main__':
    position = np.load('1_pos_time/pos_2021-08-27-20_27_21.npy')
    
    position10,position11,position12 = get_xyz(position)
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    ax.plot(position10, position11, position12)
        
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()
