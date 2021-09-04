import numpy as np
import matplotlib.pyplot as plt
from Visualize_data_3d import plot_vel_z as plot_vel_z_sin

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
    
    position12 = Z_up(position12)
    position22 = Z_up(position22)    
    position32 = Z_up(position32)
    
    position12 = Z_zero(position12)
    position22 = Z_zero(position22)    
    position32 = Z_zero(position32)
    
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
    
def Z_rotation(pos1,pos2,pos3):
    pass

def Z_up(pos_z):
    for i in range(len(pos_z)):
        pos_z[i] = -pos_z[i]
    return pos_z

def Z_zero(pos_z):
    zero = pos_z[0]
    for i in range(len(pos_z)):
        pos_z[i] = pos_z[i] - zero
    return pos_z         

def path_name(flag,data_folder = 'pos_vel_time/',name_date = '_2021-08-29-',name_time = '00_39_47'):    
    
    
    name_var11 = 'pos1'
    name_var12 = 'pos2'
    name_var13 = 'pos3'
    name_var21 = 'time1'
    name_var22 = 'time2'
    name_var23 = 'time3'
    name_var31 = 'velocity1'
    name_var32 = 'velocity2'
    name_var33 = 'velocity3'
    
    
    # name_time = '00_58_50'
    
    name_type = '.npy'
    
    f_name11 = data_folder + name_var11 + name_date + name_time + name_type
    f_name12 = data_folder + name_var12 + name_date + name_time + name_type
    f_name13 = data_folder + name_var13 + name_date + name_time + name_type
    f_name21 = data_folder + name_var21 + name_date + name_time + name_type
    f_name22 = data_folder + name_var22 + name_date + name_time + name_type
    f_name23 = data_folder + name_var23 + name_date + name_time + name_type
    f_name31 = data_folder + name_var31 + name_date + name_time + name_type
    f_name32 = data_folder + name_var32 + name_date + name_time + name_type
    f_name33 = data_folder + name_var33 + name_date + name_time + name_type
    
    if flag == 'pos':
        return f_name11,f_name12,f_name13
    elif flag == 'time':
        return f_name21,f_name22,f_name23
    elif flag == 'vel':
        return f_name31,f_name32,f_name33

def xy_pos(position10,position11):
    x = position10
    y = position11
    xy_list = []
    for i in range(len(x)):
        xy = np.sqrt(x[i]**2 + y[i]**2)
        xy_list.append(xy)
    return xy_list 

def cal_vel(time1,pos_xy):    
    # pos_xy = position1xy
    vel_xy = []
    for i in range(1,len(pos_xy)):
        velocity_xy = (pos_xy[i] - pos_xy[i-1])/ (time1[i] - time1[i-1])
        vel_xy.append(velocity_xy)
    return vel_xy   

def cal_vel_dt(time1,pos_xy):    
    # pos_xy = position1xy
    vel_xy = []
    for i in range(1,len(pos_xy)):
        velocity_xy = (pos_xy[i] - pos_xy[i-1])/ (0.01)
        vel_xy.append(velocity_xy)
    return vel_xy   

def plot_vel_xy(time1,position10,position11):
    position1xy = xy_pos(position10,position11)
    
    vel1_xy = cal_vel(time1,position1xy)
    
    # vel1_xy_dt = cal_vel_dt(time1,position1xy)
    
    time = time1[1:]
    fig = plt.figure()
    plt.scatter(time,vel1_xy)
    plt.show()   

def plot_vel_z(time1,position12):

    
    vel1_z = cal_vel(time1,position12)
    
    # vel1_xy_dt = cal_vel_dt(time1,position1xy)
    
    time = time1[1:]
    fig = plt.figure()
    plt.scatter(time,vel1_z)
    plt.show()   
    
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
    

    # 58_50
    # 53_20
    # 50_37
    # 46_48
    
    # 44_44 
    # 43_24
    
    # 41_07
    # 39_47
    """
    position1 = np.load('pos_vel_time/pos1_2021-08-29-00_58_50.npy')
    position2 = np.load('pos_vel_time/pos2_2021-08-29-00_58_50.npy')
    position3 = np.load('pos_vel_time/pos3_2021-08-29-00_58_50.npy')
    
    time1 = np.load('pos_vel_time/time1_2021-08-29-00_24_24.npy')
    time2 = np.load('pos_vel_time/time2_2021-08-29-00_24_24.npy')
    time3 = np.load('pos_vel_time/time3_2021-08-29-00_24_24.npy')
    """
    
    # pos1_2021-08-26-13_38_58
    
    data_folder = 'pos_vel_time/'    
    #data_folder = 'pos_time/'
    #data_folder = 'data/'
    name_date = '_2021-08-27-'
    name_date = '_2021-08-29-'
    #name_date = '_2021-08-26-'
    name_time = '20_36_51'
    #name_time = '13_38_58'
    name_time = '00_43_24'
    
    name_flag1 = 'pos'
    name_flag2 = 'time'
    name_flag3 = 'vel'
    
    switch = 0
    plot_max = 1
    
    pos_name1,pos_name2,pos_name3 = path_name(name_flag1,data_folder,name_date,name_time) 
    
    if switch == 1:
        time_name1,time_name2,time_name3 = path_name(name_flag2,data_folder,name_date,name_time)
    
    if switch == 2:
        time_name1,time_name2,time_name3 = path_name(name_flag2,data_folder,name_date,name_time)
        vel_name1,vel_name2,vel_name3 = path_name(name_flag3,data_folder,name_date,name_time)
    
    position1 = np.load(pos_name1)
    position2 = np.load(pos_name2)
    position3 = np.load(pos_name3)
    
    if switch == 1:
        time1 = np.load(time_name1)
        time2 = np.load(time_name2)
        time3 = np.load(time_name3)         
    
    if switch == 2:
        time1 = np.load(time_name1)
        time2 = np.load(time_name2)
        time3 = np.load(time_name3) 
        vel1 = np.load(vel_name1)
        vel2 = np.load(vel_name2)
        vel3 = np.load(vel_name3)    
    
    flag = "3d_plot"
    visual_diff_3d_plot(flag,position1,position2,position3,XYZ_max=plot_max)
    
    flag = "3d_scatter"
    visual_diff_3d_plot(flag,position1,position2,position3,XYZ_max=plot_max)
    
    position10,position11,position12 = get_xyz(position1)    
    position20,position21,position22 = get_xyz(position2)
    position30,position31,position32 = get_xyz(position3)
    
    
    if switch == 2:
        plot_vel_xy(time2,position20,position21)
    
        plot_vel_z(time1,position12)
    
    plot_vel_z_sin(position12)    
    
    """
    position12 = Z_up(position12)
    position22 = Z_up(position22)    
    position32 = Z_up(position32)
    
    position12_0 = Z_zero(position12)
    position22_0 = Z_zero(position22)    
    position32_0 = Z_zero(position32)
    """
    """
    pos_z_ave = (position12[0] + position22[0] + position32[0])/3
    
    diff_z1 = position12[0] - pos_z_ave
    diff_z2 = position22[0] - pos_z_ave
    diff_z3 = position32[0] - pos_z_ave
    """
    
    
    
    
        
    
    

    


        
    
   
    
    
