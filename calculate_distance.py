import os
import csv
import numpy as np
import matplotlib.pyplot as plt
import math
from const import * 

def to_dbm(watt):
    return 10 * np.log10(watt) + 30

def to_watt(dbm):
    return np.divide((10 ** (np.divide(dbm, 10))), 1000)

def k_value(signal, dis):
    wat = to_watt(signal)
    k = (wat) * dis * dis
    return k

def rssi_func(k, t):
    return to_dbm(k / (t ** 2))
    # return k / (t ** 2)
    
def rssi_to_dis(k, signal):
    signal = to_watt(signal)
    dis = math.sqrt(k / signal)
    return dis
    
if __name__ == "__main__":
    dir = os.listdir('./data/RSSI')
    dic = {}
    k_org = 1.4858080060144432e-06
    k_mod = 1.878343380171123e-06
    partition = 2
    for f in dir:
        f_path = './data/RSSI/' + f
        data = []
        with open(f_path) as csvfile:
            reader = csv.reader(csvfile, delimiter='\n')
            for row in reader:
                data.append(eval(row[0]))
        dic[f] = data
    
    
    error_lst_org = []
    error_lst_mod = []
    error_lst_with_acc_org = []
    error_lst_with_acc_mod = []
    distance_error_dic_org = {}
    distance_error_dic_mod = {}
    distance_error_dic_with_acc_org = {}
    distance_error_dic_with_acc_mod = {}
    
    
    dis_acc = {
        '0.804': 0.82, 
        '0.842': 0.84, 
        '0.923': 0.91, 
        '1.182': 1.21, 
        '1.20': 1.21, 
        '1.225': 1.23, 
        '1.57': 1.58, 
        '1.578': 1.56, 
        '1.628': 1.61,
        '2.028': 2.02,
        '2.062': 2.01,
        '2.082': 2.07,
        '2.406': 2.40,
        '2.408': 2.39,
        '2.453': 2.45,
        '2.804': 2.79,
        '2.858': 2.86,
        '2.939': 2.90,
        '3.420': 3.45,
        '3.424': 3.43,
        '3.481': 3.43,
        '3.847': 3.86,
        '3.884': 3.91,
        '3.941': 3.90
    }
    max_speed = {
        '0.804': 1.14, 
        '0.842': 1.07, 
        '0.923': 1.32, 
        '1.182': 1.08, 
        '1.20': 1.35, 
        '1.225': 1.23, 
        '1.57': 1.17, 
        '1.578': 1.42, 
        '1.628': 1.47,
        '2.028': 1.47,
        '2.062': 1.32,
        '2.082': 1.51,
        '2.406': 1.32,
        '2.408': 1.24,
        '2.453': 1.56,
        '2.804': 1.43,
        '2.858': 1.56,
        '2.939': 1.53,
        '3.420': 1.39,
        '3.424': 1.54,
        '3.481': 1.45,
        '3.847': 1.29,
        '3.884': 1.34,
        '3.941': 1.29
    }
    init_pos = {
        '0.804': 0.5, 
        '0.842': 0.5, 
        '0.923': 0.5,  
        '1.182': 0.85,
        '1.20': 0.85, 
        '1.225': 0.85, 
        '1.57': 1.2, 
        '1.578': 1.2, 
        '1.628': 1.2,
        '2.028': 1.6,
        '2.062': 1.6,
        '2.082': 1.6,
        '2.406': 2.0,
        '2.408': 2.0,
        '2.453': 2.0,
        '2.804': 2.4,
        '2.858': 2.4,
        '2.939': 2.4,
        '3.420': 3.0,
        '3.424': 3.0,
        '3.481': 3.0,
        '3.847': 3.5,
        '3.884': 3.5,
        '3.941': 3.5
    }
    time_slots = {
        '0.804': 30, 
        '0.842': 29, 
        '0.923': 31, 
        '1.182': 32,
        '1.20': 28, 
        '1.225': 30, 
        '1.57': 33, 
        '1.578': 31, 
        '1.628': 31,
        '2.028': 31,
        '2.062': 31,
        '2.082': 30,
        '2.406': 26,
        '2.408': 28,
        '2.453': 31,
        '2.804': 30,
        '2.858': 31,
        '2.939': 35,
        '3.420': 32,
        '3.424': 28,
        '3.481': 31,
        '3.847': 28,
        '3.884': 39,
        '3.941': 32
    }
    for dist in dic:
        signal_lst_org = dic[dist]
        signal_lst_org.sort(reverse=True)
        signal_lst_mod = signal_lst_org[:len(signal_lst_org) // partition]
        estimate_distance_value_org = rssi_to_dis(k_org, sum(signal_lst_org) / len(signal_lst_org))
        estimate_distance_value_mod = rssi_to_dis(k_mod, sum(signal_lst_mod) / len(signal_lst_mod))
        estimate_distance_value_with_acc_org = (estimate_distance_value_org + dis_acc[dist]) / 2
        estimate_distance_value_with_acc_mod = (estimate_distance_value_mod + dis_acc[dist]) / 2
        distance_error_dic_mod[dist] = abs(estimate_distance_value_mod - eval(dist))
        error_lst_mod.append(abs(estimate_distance_value_mod - eval(dist)))
        error_lst_with_acc_mod.append(abs(estimate_distance_value_with_acc_mod - eval(dist)))
        distance_error_dic_org[dist] = abs(estimate_distance_value_org - eval(dist))
        error_lst_org.append(abs(estimate_distance_value_org - eval(dist)))
        error_lst_with_acc_org.append(abs(estimate_distance_value_with_acc_org - eval(dist)))
        distance_error_dic_with_acc_org[dist] = abs(estimate_distance_value_with_acc_org - eval(dist))
        distance_error_dic_with_acc_mod[dist] = abs(estimate_distance_value_with_acc_mod - eval(dist))
        max_pos = init_pos[dist] + max_speed[dist] * time_slots[dist] * 0.02
        max_rssi = rssi_func(k_org, init_pos[dist])
        min_rssi = rssi_func(k_org, max_pos)
        bound_org = []
        for rssi in signal_lst_org:
            if rssi >= min_rssi and rssi <= max_rssi:
                bound_org.append(rssi)
        max_rssi_mod = rssi_func(k_mod, init_pos[dist])
        min_rssi_mod = rssi_func(k_mod, max_pos)
        bound_mod = []
        for rssi in signal_lst_mod:
            if rssi >= min_rssi_mod and rssi <= max_rssi_mod:
                bound_mod.append(rssi)
        print(f"Location : {eval(dist):.3f}, Bounded len: {len(bound_mod)}, Original len: {len(signal_lst_mod)}, Estimate Pos: {estimate_distance_value_mod:.3f}, Error: {distance_error_dic_mod[dist]:.3f}, Max: {max_rssi_mod}, Min: {min_rssi_mod}")
        print(f"Location : {eval(dist):.3f}, Bounded len: {len(bound_org)}, Original len: {len(signal_lst_org)}, Estimate Pos: {estimate_distance_value_org:.3f}, Error: {distance_error_dic_org[dist]:.3f}, Max: {max_rssi}, Min: {min_rssi}")
        
    error_lst_mod.sort()
    error_lst_org.sort()
    error_lst_with_acc_mod.sort()
    error_lst_with_acc_org.sort()
    cdf_lst = [x / (len(error_lst_org)) for x in range(len(error_lst_org) + 1)]
    dis_list = [eval(x) for x in dis_acc.keys()]
    error_dis_lst_org = [distance_error_dic_org[x] for x in dis_acc.keys()]
    error_dis_lst_mod = [distance_error_dic_mod[x] for x in dis_acc.keys()]
    error_dis_lst_with_acc_org = [distance_error_dic_with_acc_org[x] for x in dis_acc.keys()]
    error_dis_lst_with_acc_mod = [distance_error_dic_with_acc_mod[x] for x in dis_acc.keys()]
    error_lst_org.insert(0, 0)
    error_lst_mod.insert(0, 0)
    error_lst_with_acc_org.insert(0, 0)
    error_lst_with_acc_mod.insert(0, 0)
    print(error_dis_lst_org)
    print(error_dis_lst_mod)
    plt.figure(figsize=FIG_SIZE, dpi=DPI)
    plt.scatter(x=dis_list, y=error_dis_lst_org, label='Base', marker='>', s=MARKER_SIZE)
    plt.scatter(x=dis_list, y=error_dis_lst_mod, label='50%', marker='o', s=MARKER_SIZE)
    plt.xlabel('Distance (m)', fontsize=LEGEND_FONT_SIZE)
    plt.ylabel('Error (m)', fontsize=LEGEND_FONT_SIZE)
    plt.grid()
    plt.ylim(bottom=0)
    plt.legend(loc="best", fontsize=LEGEND_FONT_SIZE)
    plt.xticks(fontsize=TICKS_FONT_SIZE)
    plt.yticks(fontsize=TICKS_FONT_SIZE)
    plt.savefig('error_dis.png')
    plt.savefig('error_dis.pdf')
    
    
    plt.figure(figsize=FIG_SIZE, dpi=DPI)
    plt.scatter(x=dis_list, y=error_dis_lst_org, label='Base', marker='>', s=MARKER_SIZE)
    plt.scatter(x=dis_list, y=error_dis_lst_mod, label='50%', marker='o', s=MARKER_SIZE)
    plt.scatter(x=dis_list, y=error_dis_lst_with_acc_org, label='Base + acc', marker='s', s=MARKER_SIZE)
    plt.scatter(x=dis_list, y=error_dis_lst_with_acc_mod, label='50% + acc', marker='8', s=MARKER_SIZE)
    plt.xlabel('Distance (m)', fontsize=LEGEND_FONT_SIZE)
    plt.ylabel('Error (m)', fontsize=LEGEND_FONT_SIZE)
    plt.grid()
    plt.ylim(bottom=0)
    plt.legend(loc="best", fontsize=LEGEND_FONT_SIZE)
    plt.xticks(fontsize=TICKS_FONT_SIZE)
    plt.yticks(fontsize=TICKS_FONT_SIZE)
    plt.savefig('error_dis_with_acc.png')
    plt.savefig('error_dis_with_acc.pdf')
    
    plt.figure(figsize=FIG_SIZE, dpi=DPI)
    plt.plot(error_lst_org, cdf_lst, label='Base', linewidth=LINE_WIDTH)
    plt.plot(error_lst_mod, cdf_lst, label='50%', linewidth=LINE_WIDTH)
    plt.plot(error_lst_with_acc_org, cdf_lst, label='Base + acc', linewidth=LINE_WIDTH)
    plt.plot(error_lst_with_acc_mod, cdf_lst, label='50% + acc', linewidth=LINE_WIDTH)
    plt.xlabel('Error (m)', fontsize=LEGEND_FONT_SIZE)
    plt.ylabel('CDF', fontsize=LEGEND_FONT_SIZE)
    plt.grid()
    plt.ylim((0, 1))
    plt.xlim((0, 4))
    plt.legend(loc="best", fontsize=LEGEND_FONT_SIZE)
    plt.xticks(fontsize=TICKS_FONT_SIZE)
    plt.yticks(fontsize=TICKS_FONT_SIZE)
    plt.savefig('cdf.png')
    plt.savefig('cdf.pdf')
        