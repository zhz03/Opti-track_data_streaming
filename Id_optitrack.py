import Optitrack as OptiT
import numpy as np
import time
import sys

if __name__ == '__main__':
    op = OptiT.OptiTrack()

    current_time = time.time()
    position1 = []
    position2 = []
    position3 = []
    time1 = []
    time2 = []
    time3 = []
    
    id1 = 27
    id2 = 28
    id3 = 29
    velocity = []
    begin_time = time.time()
    
    while True:

        pass
        if time.time() - current_time >= 0.01: # 0.1 second refresh rate
            #print('position = %s' % (op.position))
            if op.id == id1:
            	time1.append(current_time)
            	position1.append(op.position)
            elif op.id == id2:
            	time2.append(current_time)
            	position2.append(op.position)
            else:
            	time3.append(current_time)
            	position3.append(op.position)
            current_time = time.time()
	    # print('id =%s, position = %s' % (op.id,))
	    
	    
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        
        if time.time() - begin_time >= 10:
            now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
            #np.save('position.npy',position)
            
            np.save(f'pos_time/pos1_{now}.npy', position1)
            np.save(f'pos_time/pos2_{now}.npy', position2)
            np.save(f'pos_time/pos3_{now}.npy', position3)
            
            np.save(f'pos_time/time1_{now}.npy', time1)
            np.save(f'pos_time/time2_{now}.npy', time2)
            np.save(f'pos_time/time3_{now}.npy', time3)
            
            print("save .npy done")
            sys.exit()
        
