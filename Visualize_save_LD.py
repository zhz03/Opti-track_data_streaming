import Optitrack as OptiT
import numpy as np
import time
import sys
import matplotlib.pyplot as plt

if __name__ == '__main__':
    op = OptiT.OptiTrack()

    current_time = time.time()
    position = []
    velocity = []
    begin_time = time.time()
    fig = plt.figure()
    plt.ion()
    position0 = []
    position1 = []
    while True:
        
        pass
        if time.time() - current_time >= 0.01: # 0.01 second refresh rate
            plt.clf()
            #print('position = %s' % (op.position))
            position.append(op.position)
            velocity.append(op.velocity)
            position0.append(op.position[0])
            position1.append(op.position[1])
            current_time = time.time()
            #ax.scatter(op.position[0], op.position[1], op.position[2])
            plt.scatter(position0,position1)
            plt.draw()
            #time.sleep(0.01)
            plt.pause(0.01)
        if time.time() - begin_time >= 10:
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            #np.save('position.npy',position)
            np.save(f'data/pos_{now}.npy', position)
            np.save(f'data/vel_{now}.npy', velocity)
            print("save .npy done")  
            sys.exit()      
            
                
    
