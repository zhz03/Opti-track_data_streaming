import numpy as np
import matplotlib.pyplot as plt

def get_xyz(position):
    position10 = []
    position11 = []
    position12 = []
    for i in range(len(position)):
        position10.append(position[i][0])
        position11.append(position[i][1])
        position12.append(position[i][2])
    
    return position10,position11,position12

def path_name(flag,data_folder = '1_pos_time/',name_date = '_2021-08-27-',name_time = '20_27_21'):    
    
    
    name_var1 = 'pos'
    name_var2 = 'time'
    name_var3 = 'velocity'

    
    
    # name_time = '00_58_50'
    
    name_type = '.npy'
    
    f_name11 = data_folder + name_var1 + name_date + name_time + name_type

    f_name21 = data_folder + name_var2 + name_date + name_time + name_type

    f_name31 = data_folder + name_var3 + name_date + name_time + name_type

    
    if flag == 'pos':
        return f_name11
    elif flag == 'time':
        return f_name21
    elif flag == 'vel':
        return f_name31

def plot_pos(position,XYZ_max, XYZ_min):
    position10,position11,position12 = get_xyz(position)
    
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    
    ax.plot(position10, position11, position12)
        
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    
    #XYZ_max = 1
    ax.auto_scale_xyz([-XYZ_min, XYZ_max], [-XYZ_min, XYZ_max], [-XYZ_min, XYZ_max])
    plt.show()    

def xy_pos(position10,position11):
    x = position10
    y = position11
    xy_list = []
    for i in range(len(x)):
        xy = np.sqrt(x[i]**2 + y[i]**2)
        xy_list.append(xy)
    return xy_list 

def cal_vel_dt(pos_xy):    
    # pos_xy = position1xy
    vel_xy = []
    for i in range(1,len(pos_xy)):
        velocity_xy = (pos_xy[i] - pos_xy[i-1])/ (0.01)
        vel_xy.append(velocity_xy)
    return vel_xy  

def plot_vel_xy(position10,position11):
    position1xy = xy_pos(position10,position11)
    
    vel1_xy = cal_vel_dt(position1xy)
    
    # vel1_xy_dt = cal_vel_dt(time1,position1xy)
    
    time = np.linspace(0,10,len(vel1_xy))
    fig = plt.figure()
    plt.scatter(time,vel1_xy)
    plt.show()  

def plot_vel_z(position_z):
    vel1_z = cal_vel_dt(position_z)
    time = np.linspace(0,10,len(vel1_z))
    fig = plt.figure()
    plt.scatter(time,vel1_z)
    plt.show()      
    
if __name__ == '__main__':
    
    
    #position = np.load('1_pos_time/pos_2021-08-27-20_27_21.npy')
    
    data_folder = '1_pos_time/'
    name_date = '_2021-08-31-'
    name_time = '15_43_32'
    
    
    name_flag1 = 'pos'
    pos_name = path_name(name_flag1,data_folder,name_date,name_time)
    name_flag1 = 'vel'
    vel_name = path_name(name_flag1,data_folder,name_date,name_time)

    position = np.load(pos_name)   
    
    plot_pos(position,4,2)
    
    position10,position11,position12 = get_xyz(position)
    pos_xy = xy_pos(position10,position11)
    
    val_xy = cal_vel_dt(pos_xy)
    
    #plot_vel_xy(position10,position11)
    
    #plot_vel_z(position12)
    
    
    
    
    
    
    
