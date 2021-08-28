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
    
    
if __name__ == '__main__':
    position1 = np.load('data/pos1_2021-08-26-13_38_58.npy')
    position2 = np.load('data/pos2_2021-08-26-13_38_58.npy')
    position3 = np.load('data/pos3_2021-08-26-13_38_58.npy')
    
    flag = "3d_scatter"
    visual_diff_3d_plot(flag,position1,position2,position3)
    
    

    


        
    
   
    
    
