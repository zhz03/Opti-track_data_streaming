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
    plt.ion()
    position0 = []
    position1 = []
    while True:
        
        pass
        if time.time() - current_time >= 0.01: # 0.1 second refresh rate
            plt.clf()
            #print('position = %s' % (op.position))
            position0.append(op.position[0])
            position1.append(op.position[1])
            current_time = time.time()
            #ax.scatter(op.position[0], op.position[1], op.position[2])
            plt.scatter(position0,position1)
            plt.draw()
            #time.sleep(0.01)
            plt.pause(0.01)
            
                
    
