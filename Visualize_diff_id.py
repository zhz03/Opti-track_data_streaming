import numpy as np
import matplotlib.pyplot as plt

def visual_diff_3d_scatter(position1,position2,position3):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    t = min(len(position1),len(position2),len(position3))
    for i in range(t):
        ax.scatter(position1[i][0], position1[i][1], position1[i][2])
        ax.scatter(position2[i][0], position2[i][1], position2[i][2])
        ax.scatter(position3[i][0], position3[i][1], position3[i][2])
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()    

def get_xyz(position):
    position10 = []
    position11 = []
    position12 = []
    for i in range(len(position)):
        position10.append(position[i][0])
        position11.append(position[i][1])
        position12.append(position[i][2])
    
    return position10,position11,position12

def visual_diff_3d_plot(flag,position1,position2,position3):
    position10 = [] # x
    position11 = [] # y
    position12 = [] # z
    
    position20 = [] 
    position21 = []
    position22 = []
    
    position30 = [] 
    position31 = []
    position32 = []
    
    position10,position11,position12 = get_xyz(position1)    
    position20,position21,position22 = get_xyz(position2)
    position30,position31,position32 = get_xyz(position3)
    """
    position12 = Z_up(position12)
    position22 = Z_up(position22)    
    position32 = Z_up(position32)
    
    position12 = Z_zero(position12)
    position22 = Z_zero(position22)    
    position32 = Z_zero(position32)
    """
    fig = plt.figure()
    
 
    
    if flag == "2d":
        plt.xlabel("X label")
        plt.ylabel("Y label")
        plt.plot(position10,position11)
        plt.plot(position20,position21)
        plt.plot(position30,position31)
    
    #plt.plot(position10,position12)
    #plt.plot(position20,position22)
    #plt.plot(position30,position32)
    elif flag == "3d_plot":
        ax = fig.add_subplot(projection='3d')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')  
        ax.plot(position10, position11, position12)
        ax.plot(position20, position21, position22)
        ax.plot(position30, position31, position32)
    elif flag == "3d_scatter":
        ax = fig.add_subplot(projection='3d')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')  
        ax.scatter(position10, position11, position12)
        ax.scatter(position20, position21, position22)
        ax.scatter(position30, position31, position32)
    plt.show()        
    
def Z_rotation(pos1,pos2,pos3):
    pass

def Z_up(pos_z):
    for i in range(len(pos_z)):
        pos_z[i] = -pos_z[i]
    return pos_z

def Z_zero(pos_z):
    for i in range(len(pos_z)):
        pos_z[i] = pos_z[i] - pos_z[0]
    return pos_z         
    
if __name__ == '__main__':
    """
    position1 = np.load('data/pos1_2021-08-26-13_38_58.npy')
    position2 = np.load('data/pos2_2021-08-26-13_38_58.npy')
    position3 = np.load('data/pos3_2021-08-26-13_38_58.npy')
    """
    """
    position1 = np.load('pos_time/pos1_2021-08-27-20_36_51.npy')
    position2 = np.load('pos_time/pos2_2021-08-27-20_36_51.npy')
    position3 = np.load('pos_time/pos3_2021-08-27-20_36_51.npy')
    
    time1 = np.load('pos_time/time1_2021-08-27-20_36_51.npy')
    time2 = np.load('pos_time/time2_2021-08-27-20_36_51.npy')
    time3 = np.load('pos_time/time3_2021-08-27-20_36_51.npy')    
    """
    # 
    # 50_37
    # 46_48
    
    # 44_44 
    # 43_24
    
    # 41_07
    # 39_47
    position1 = np.load('pos_vel_time/pos1_2021-08-29-00_58_50.npy')
    position2 = np.load('pos_vel_time/pos2_2021-08-29-00_58_50.npy')
    position3 = np.load('pos_vel_time/pos3_2021-08-29-00_58_50.npy')
    
    time1 = np.load('pos_vel_time/time1_2021-08-29-00_24_24.npy')
    time2 = np.load('pos_vel_time/time2_2021-08-29-00_24_24.npy')
    time3 = np.load('pos_vel_time/time3_2021-08-29-00_24_24.npy')    
    
    flag = "3d_plot"
    visual_diff_3d_plot(flag,position1,position2,position3)

    flag = "3d_scatter"
    visual_diff_3d_plot(flag,position1,position2,position3)

    position10,position11,position12 = get_xyz(position1)    
    position20,position21,position22 = get_xyz(position2)
    position30,position31,position32 = get_xyz(position3)
    
    position12 = Z_up(position12)
    position22 = Z_up(position22)    
    position32 = Z_up(position32)
    
    position12 = Z_zero(position12)
    position22 = Z_zero(position22)    
    position32 = Z_zero(position32)
    
    pos_z_ave = (position12[0] + position22[0] + position32[0])/3
    
    diff_z1 = position12[0] - pos_z_ave
    diff_z2 = position22[0] - pos_z_ave
    diff_z3 = position32[0] - pos_z_ave
    
    
        
    
    

    


        
    
   
    
    
