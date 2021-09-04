import numpy as np
import matplotlib.pyplot as plt
from Visualize_diff_id import path_name,visual_diff_3d_plot,get_xyz,Z_up,Z_zero

from math import sqrt, pow, acos

def angle_of_vector(v1, v2):
    pi = 3.1415
    vector_prod = v1[0] * v2[0] + v1[1] * v2[1]
    length_prod = sqrt(pow(v1[0], 2) + pow(v1[1], 2)) * sqrt(pow(v2[0], 2) + pow(v2[1], 2))
    cos = vector_prod * 1.0 / (length_prod * 1.0 + 1e-6)
    return (acos(cos) / pi) * 180

def cal_vec_3p(init_ind,position_1,position_2,position_3):    
    # init_ind = 0
    
    mid_point0 = (position_1[0][init_ind] + position_2[0][init_ind])/2
    mid_point1 = (position_1[1][init_ind] + position_2[1][init_ind])/2
    
    vec1 = [position_3[0][init_ind]-mid_point0,position_3[1][init_ind]-mid_point1]
    
    mid_point = [mid_point0,mid_point1]
    # vec2 = 
    return vec1,mid_point 

def cal_vec_2p(init_ind,position_1,position_2):
    vec = [position_2[0][init_ind]-position_1[0][init_ind],position_2[1][init_ind] - position_1[1][init_ind]]
    
    return vec

def visualize_vec_3p(ind_list,position_1,position_2,position_3,mid_point_list):
    # ind_list = [0,-1]
    fig = plt.figure()
    
    for i in range(len(ind_list)):
        plt.scatter(position_1[0][ind_list[i]],position_1[1][ind_list[i]],c = 'r')
    for i in range(len(ind_list)):
        plt.scatter(position_2[0][ind_list[i]],position_2[1][ind_list[i]],c='b')
    for i in range(len(ind_list)):
        plt.scatter(position_3[0][ind_list[i]],position_3[1][ind_list[i]],c ='g')  
    for i in range(len(mid_point_list)):
        plt.scatter(mid_point_list[i][0],mid_point_list[i][1],c = 'k')
    plt.show()

def combine_xyz(position_10,position_11,position_12):    
    position_1 = []
    position_1.append(position_10)
    position_1.append(position_11)
    position_1.append(position_12)
    return position_1

def combine_xyz_array(position_10,position_11,position_12):
    position_1 = np.empty(shape=(1,3),dtype=float)
    for i in range(len(position_10)):
        pos_1 = np.array([position_10[i],position_11[i],position_12[i]])
        position_1 = np.vstack((position_1,pos_1))
    return position_1

def cal_vec_ang(ind_list,position_1,position_2,position_3,v_flag = 0):    
    # ind_list = [0,-1]
    
    init_ind1 = ind_list[0]
    vec1,midp1 = cal_vec_3p(init_ind1,position_1,position_2,position_3)
    
    init_ind2 = ind_list[1]
    vec2,midp2 = cal_vec_3p(init_ind2,position_1,position_2,position_3)
    
    ang = angle_of_vector(vec1, vec2)
    
    mid_ps = []
    mid_ps.append(midp1)
    mid_ps.append(midp2)

    if v_flag != 0:
        visualize_vec_3p(ind_list,position_1,position_2,position_3,mid_ps)
    
    return ang     

if __name__ == '__main__':
    # data_folder = 'pos_vel_time/'    
    #data_folder = 'pos_time/'
    data_folder = 'data/'
    name_date = '_2021-08-27-'
    name_date = '_2021-08-29-'
    name_date = '_2021-08-26-'
    name_time = '20_36_51'
    name_time = '13_38_58'
    # name_time = '00_43_24'
    
    name_flag1 = 'pos'
    name_flag2 = 'time'
    name_flag3 = 'vel'
    
    switch = 0
    plot_max = 0
    
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
    
    
    position10,position11,position12 = get_xyz(position1)    
    position20,position21,position22 = get_xyz(position2)
    position30,position31,position32 = get_xyz(position3)

    position12 = Z_up(position12)
    position22 = Z_up(position22)    
    position32 = Z_up(position32)
    
    position12 = Z_zero(position12)
    position22 = Z_zero(position22)    
    position32 = Z_zero(position32)
    
    position_1 = combine_xyz(position10,position11,position12)
    position_2 = combine_xyz(position20,position21,position22)
    position_3 = combine_xyz(position30,position31,position32)
    
    position_1_a = combine_xyz_array(position10,position11,position12)
    
    
    ind_list = [0,-1]
    
    ang1 = cal_vec_ang(ind_list,position_1,position_2,position_3,v_flag = 1)

    ang2 = cal_vec_ang(ind_list,position_1,position_3,position_2,v_flag = 1)
    
    ang2 = cal_vec_ang(ind_list,position_1,position_3,position_2,v_flag = 1)
    
    ang3 = cal_vec_ang(ind_list,position_2,position_3,position_1,v_flag = 1)
    
    init_ind= 0
    
    vec1 = cal_vec_2p(init_ind,position_1,position_2)
    
    init_ind = -1
    vec2 = cal_vec_2p(init_ind,position_1,position_2)
    
    ang = angle_of_vector(vec1, vec2)
    
    #position_1=list([[1],[1]])
    #position_2 = list([[2],[1]])
    #vec = cal_vec_2p(init_ind,position_1,position_2)
    
    
    


    

