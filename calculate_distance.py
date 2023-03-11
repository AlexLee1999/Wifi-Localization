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
    k_mod = 2.6515100662316045e-06
    partition = 10
    for f in dir:
        f_path = './data/RSSI/' + f
        data = []
        with open(f_path) as csvfile:
            reader = csv.reader(csvfile, delimiter='\t')
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
    dis_acc = {'0.804': 0.82, 
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
               '3.941': 3.90}
    for dist in dic:
        sig = dic[dist]
        sig.sort(reverse=True)
        sig_mod = sig[:len(sig) // partition]
        estimate_org = rssi_to_dis(k_org, sum(sig) / len(sig))
        estimate_mod = rssi_to_dis(k_mod, sum(sig_mod) / len(sig_mod))
        acc_org = (estimate_org + dis_acc[dist]) / 2
        acc_mod = (estimate_mod + dis_acc[dist]) / 2
        # print(estimate_org, dist)
        # print(estimate_mod, dist)
        dis_error_mod[dist] = abs(estimate_mod - eval(dist))
        error_mod.append(abs(estimate_mod - eval(dist)))
        error_mod_acc.append(abs(acc_mod - eval(dist)))
        dis_error_org[dist] = abs(estimate_org - eval(dist))
        error_org.append(abs(estimate_org - eval(dist)))
        error_org_acc.append(abs(acc_org - eval(dist)))
    # print(dis_error_org)
    # print(dis_error_mod)
    error_mod.sort()
    error_org.sort()
    error_mod_acc.sort()
    error_org_acc.sort()
    # print(error_org)
    # print(error_mod)
    print(error_mod_acc)
    print(error_org_acc)
    cdf_lst = [x / (len(error_org)) for x in range(1, len(error_org) + 1)]
    # print(cdf_lst)
    
    
    plt.figure()
    plt.plot(error_org, cdf_lst, label='Base')
    plt.plot(error_mod, cdf_lst, label='10%')
    plt.plot(error_org_acc, cdf_lst, label='Base + acc')
    plt.plot(error_mod_acc, cdf_lst, label='10% + acc')
    plt.legend(loc="best")
    plt.savefig('cdf.png')
        