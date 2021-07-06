import Optitrack as OptiT
import numpy as np
import time
import sys

if __name__ == '__main__':
    op = OptiT.OptiTrack()

    current_time = time.time()
    position = []
    begin_time = time.time()
    while True:

        pass
        if time.time() - current_time >= 0.1: # 0.1 second refresh rate
            #print('position = %s' % (op.position))
            position.append(op.position)
            current_time = time.time()
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        if time.time() - begin_time >= 5:
            #np.save('position.npy',position)
            np.save(f'data/{time.time()}.npy', position)
            print("save .npy done")
            sys.exit()