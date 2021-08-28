import Optitrack as OptiT
import numpy as np
import time
import sys

def id_parse():
    id1 = 0
    id2 = 0
    id3 = 0
    current_time = time.time()
    begin_time = time.time()
    count = 0
    while count ==0: 
        pass
        if time.time() - current_time > 0.01:
            ID = op.id
            if id1 == 0:
                a = ID
                id1 = a
            elif id1 != 0 and id2 == 0:
                b = ID
                if b != id1:
                    id2 = b
            elif id1 != 0 and id2 != 0:
                c = ID
                if c != id1 and c != id2:
                    id3 = c

 
            
            current_time = time.time()
        
        if time.time() - begin_time >= 5:
            count +=1 
            print("id parsing finish")
    """
    print(f"id1:",id1)
    print(f"id2:",id2)
    print(f"id3:",id3)  
    """    
    return id1,id2,id3


if __name__ == '__main__':
    op = OptiT.OptiTrack()


    current_time = time.time()
    position1 = []
    position2 = []
    position3 = []
    time1 = []
    time2 = []
    time3 = []
    
    id1 = 0
    id2 = 0
    id3 = 0
    
    id1,id2,id3 = id_parse()
    print(f"id1:",id1)
    print(f"id2:",id2)
    print(f"id3:",id3)   
    """
    current_time = time.time()
    begin_time = time.time()
    count = 0
    while count ==0: 
        pass
        if time.time() - current_time > 0.01:
            ID = op.id
            if id1 == 0:
                a = ID
                id1 = a
            elif id1 != 0 and id2 == 0:
                b = ID
                if b != id1:
                    id2 = b
            elif id1 != 0 and id2 != 0:
                c = ID
                if c != id1 and c != id2:
                    id3 = c

 
            
            current_time = time.time()
        
        if time.time() - begin_time >= 5:
            count +=1 
            print("id parsing finish")
        
    print(f"id1:",id1)
    print(f"id2:",id2)
    print(f"id3:",id3)    
    """     

        
