import numpy as np
from matplotlib import pyplot as plt
import pandas as pd 

def combine_xyz_array(position_10,position_11,position_12):
    position_1 = np.empty(shape=(1,3),dtype=float)
    for i in range(len(position_10)):
        pos_1 = np.array([position_10[i],-position_11[i],position_12[i]])
        position_1 = np.vstack((position_1,pos_1))
    return position_1

def xzup2xyzcomb(df00,x,y,z):    
    p_x1 = dfdata_2_floatlist(df00,x) # x
    p_y1 = dfdata_2_floatlist(df00,y) # up 
    p_z1 = dfdata_2_floatlist(df00,z) # z
    
    pos1 = combine_xyz_array(p_x1,p_z1,p_y1) # xyz coordinate
    pos1 = np.delete(pos1,0, axis = 0)
    
    return pos1 

def get_xyz(position):
    position10 = []
    position11 = []
    position12 = []
    for i in range(len(position)):
        position10.append(position[i][0])
        position11.append(position[i][1])
        position12.append(position[i][2])
    
    return position10,position11,position12

def visual_diff_3d_plot(flag,position1,position2,position3,XYZ_max=2):
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
        ax.scatter(position10, position11, position12,s=1)
        ax.scatter(position20, position21, position22,s=1)
        ax.scatter(position30, position31, position32,s=1)
    if XYZ_max != 0:
        ax.auto_scale_xyz([-XYZ_max, XYZ_max], [-XYZ_max, XYZ_max], [-XYZ_max, XYZ_max])
    plt.show()        
    
def dfdata_2_floatlist(df00,c_name):
    # c_name = 'P_X1'
    P_X1 = list(df00[c_name])
    p_X1 = [float(i) for i in P_X1]
    return p_X1
    
if __name__ == '__main__':
    #Take 2021-08-31 03.24.55 PM
    name1 = 'Take '
    name2 = "2021-08-31 "
    name_time = '03.24.55'
    name_time = '04.16.48'
    #name_time = '04.26.01'
    #name_time = '04.28.09'
    name_3 = ' PM'
    name_4 = '.csv'
    #f_name = 'Take2021-08-3103.44.49PM.csv'
    f_name = name1 + name2 + name_time + name_3 + name_4 
    sheet_name = name1 + name2 + name_time + name_3
    df00 = pd.read_csv(f_name)
    
    switch = 3
    if switch == 1:
        del_col = ['Export Frame Rate', '120.000000.1', 'Capture Start Time',
           '2021-08-31 03.24.56.238 PM', 'Capture Start Frame', '183068',
           'Total Frames in Take', '2318', 'Total Exported Frames', '2318.1',
           'Rotation Type', 'YXZ', 'Length Units', 'Meters', 'Coordinate Space',
           'Global']
        
        
            
        df00.drop(df00.head(5).index,inplace=True)
        df00.drop(del_col,axis=1, inplace=True)
    
        df00.columns = ['Frame','Time (Seconds)','R_Y','R_X','R_Z','P_X','P_Y','P_Z']
    
    if switch == 3:
        del_col = ['Length Units', 'Meters', 'Coordinate Space','Global']
        df00.drop(df00.head(5).index,inplace=True)
        df00.drop(del_col,axis=1, inplace=True)
        
        df00.columns = ['Frame','Time (Seconds)','R_Y1','R_X1','R_Z1','P_X1','P_Y1','P_Z1',
                        'R_Y2','R_X2','R_Z2','P_X2','P_Y2','P_Z2',
                        'R_Y3','R_X3','R_Z3','P_X3','P_Y3','P_Z3',]
    
    index = list(df00['Frame'])
    df00.index = index
    
    time = dfdata_2_floatlist(df00,'Time (Seconds)') 
    pos1 = xzup2xyzcomb(df00,'P_X1','P_Y1','P_Z1')
    pos2 = xzup2xyzcomb(df00,'P_X2','P_Y2','P_Z2')
    pos3 = xzup2xyzcomb(df00,'P_X3','P_Y3','P_Z3')
    
    flag = "3d_plot"
    visual_diff_3d_plot(flag,pos1,pos2,pos3,XYZ_max=5)
    
    """
    p_x2 = dfdata_2_floatlist(df00,'P_X2') # x
    p_y2 = dfdata_2_floatlist(df00,'P_Y2') # up 
    p_z2 = dfdata_2_floatlist(df00,'P_Z2') # z
    
    pos1 = combine_xyz_array(p_x1,p_z1,p_y1) # xyz coordinate
    pos1 = np.delete(pos1,0, axis = 0)
    
    p_x3 = dfdata_2_floatlist(df00,'P_X3') # x
    p_y3 = dfdata_2_floatlist(df00,'P_Y3') # up 
    p_z3 = dfdata_2_floatlist(df00,'P_Z3') # z    
    """
    
    

    

    
    
    
    
    
    
