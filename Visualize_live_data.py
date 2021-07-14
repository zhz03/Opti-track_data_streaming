import Optitrack as OptiT
import numpy as np
import time
import sys
import matplotlib.pyplot as plt

if __name__ == '__main__':
    op = OptiT.OptiTrack()

    current_time = time.time()
    position = []
    begin_time = time.time()
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    while True:
        plt.clf()
        pass
        if time.time() - current_time >= 0.01: # 0.1 second refresh rate
            #print('position = %s' % (op.position))
            position.append(op.position)
            current_time = time.time()
            ax.scatter(op.position[0], op.position[1], op.position[2])
            plt.draw()
            #time.sleep(0.01)
            
                
    
