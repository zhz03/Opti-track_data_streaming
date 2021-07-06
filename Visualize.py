import Optitrack as OptiT
import time

if __name__ == '__main__':
    op = OptiT.OptiTrack()

    current_time = time.time()

    while True:
        pass
        if time.time() - current_time >= 0.1:
            print('position = %s' % (op.position))
            current_time = time.time()