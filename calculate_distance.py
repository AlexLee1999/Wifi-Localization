import os
import csv
import numpy as np
import matplotlib.pyplot as plt
import math


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
    # print(dic)
    dis_error_org = {}
    error_org = []
    error_mod = []
    error_org_acc = []
    error_mod_acc = []
    dis_error_mod = {}
    dis_acc = {
        '0.804': 0.82, 
        '0.842': 0.84, 
        '0.923': 0.91, 
        '1.20': 1.21, 
        '1.182': 1.21, 
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
        '1.20': 1.35, 
        '1.182': 1.08, 
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
        '1.20': 0.85, 
        '1.182': 0.85, 
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
        '1.20': 28, 
        '1.182': 32, 
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
        sig = dic[dist]
        sig.sort(reverse=True)
        sig_mod = sig[:len(sig) // partition]
        estimate_org = rssi_to_dis(k_org, sum(sig) / len(sig))
        estimate_mod = rssi_to_dis(k_mod, sum(sig_mod) / len(sig_mod))
        acc_org = (estimate_org + dis_acc[dist]) / 2
        acc_mod = (estimate_mod + dis_acc[dist]) / 2
        dis_error_mod[dist] = abs(estimate_mod - eval(dist))
        error_mod.append(abs(estimate_mod - eval(dist)))
        error_mod_acc.append(abs(acc_mod - eval(dist)))
        dis_error_org[dist] = abs(estimate_org - eval(dist))
        error_org.append(abs(estimate_org - eval(dist)))
        error_org_acc.append(abs(acc_org - eval(dist)))
        max_pos = init_pos[dist] + max_speed[dist] * time_slots[dist] * 0.02
        print(init_pos[dist], dist, max_pos)
        max_rssi = rssi_func(k_org, init_pos[dist])
        min_rssi = rssi_func(k_org, max_pos)
        bound_org = []
        for rssi in sig:
            if rssi >= min_rssi and rssi <= max_rssi:
                bound_org.append(rssi)
        max_rssi_mod = rssi_func(k_mod, init_pos[dist])
        min_rssi_mod = rssi_func(k_mod, max_pos)
        bound_mod = []
        for rssi in sig_mod:
            if rssi >= min_rssi_mod and rssi <= max_rssi_mod:
                bound_mod.append(rssi)
        # print(f"Location : {dist}, Bounded len: {len(bound_mod)}, Original len: {len(sig_mod)}, Error: {dis_error_mod[dist]}")
        # print(f"Location : {dist}, Bounded len: {len(bound_org)}, Original len: {len(sig)}, Error: {dis_error_org[dist]}")
        
    error_mod.sort()
    error_org.sort()
    error_mod_acc.sort()
    error_org_acc.sort()
    cdf_lst = [x / (len(error_org)) for x in range(1, len(error_org) + 1)]
    plt.figure()
    plt.plot(error_org, cdf_lst, label='Base')
    plt.plot(error_mod, cdf_lst, label='50%')
    plt.plot(error_org_acc, cdf_lst, label='Base + acc')
    plt.plot(error_mod_acc, cdf_lst, label='50% + acc')
    plt.legend(loc="best")
    plt.savefig('cdf.png')
        