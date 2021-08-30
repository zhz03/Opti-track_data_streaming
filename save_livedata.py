import Optitrack as OptiT
import numpy as np
import time
import sys

if __name__ == '__main__':
    op = OptiT.OptiTrack()

    current_time = time.time()
    position = []
    velocity = []
    time = []
        
    current_time = time.time()
    begin_time = time.time()
    while True:

        pass
        if time.time() - current_time >= 0.01: # 0.1 second refresh rate
            #print('position = %s' % (op.position))
            time.append(current_time-begin_time)
            position.append(op.position)
            velocity.append(op.velocity)
            current_time = time.time()
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        if time.time() - begin_time >= 10:
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            #np.save('position.npy',position)
            np.save(f'1_pos_time/pos_{now}.npy', position)
            np.save(f'1_pos_time/vel_{now}.npy', velocity)
            np.save(f'1_pos_time/time_{now}.npy', time)
            print("save .npy done")
            sys.exit()
