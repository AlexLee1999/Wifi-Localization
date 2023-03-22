import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
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

def OLS_func(a, c, dis):
    return a * np.log10(dis) + c
    

if __name__ == "__main__":
    k_org = []
    k_mod = [] 
    sig_org = []
    sig_mod = []
    x_org = []
    x_mod = []
    data_org = []
    data_mod = []
    partition = 2
    # Distance: 0.5
    dis = 0.5
    d = [-21, -21, -23, -22, -23, -22, -22, -23, -22, -22, -19, -18, -19, -21, -21, -19, -21, -21, -22, -27, -27, -21, -21, -19, -19, -21, -21, -22, -21, -21, -21, -22]
    d.sort(reverse=True)
    
    d_mod = d[:len(d) // partition]
    data_org.extend(d)
    data_mod.extend(d_mod)
    for i in range(len(d)):
        x_org.append(0.5)
    for _ in range(len(d_mod)):
        x_mod.append(0.5)
    print(f"AVG {sum(d) / len(d):.2f} Distance : {dis}")
    print(f"AVG {sum(d_mod) / len(d_mod):.2f} Distance : {dis}")
    sig_org.append(sum(d) / len(d))
    sig_mod.append(sum(d_mod) / len(d_mod))
    k_org.append(k_value(sum(d) / len(d), dis))
    k_mod.append(k_value(sum(d_mod) / len(d_mod), dis))
    # Distance: 0.85
    dis = 0.85
    d = [-28, -27, -32, -28, -33, -28, -27, -27, -27, -27, -27, -32, -27, -27, -27, -27, -32, -27, -27, -27, -27, -28, -27, -33, -28, -28, -28, -28, -28, -28, -27, -28, -28, -28, -27, -28, -27, -32, -28, -28, -27, -28, -28, -28]
    d.sort(reverse=True)
    d_mod = d[:len(d) // partition]
    data_org.extend(d)
    data_mod.extend(d_mod)
    for i in range(len(d)):
        x_org.append(0.85)
    for _ in range(len(d_mod)):
        x_mod.append(0.85)
    print(f"AVG {sum(d) / len(d):.2f} Distance : {dis}")
    print(f"AVG {sum(d_mod) / len(d_mod):.2f} Distance : {dis}")
    sig_org.append(sum(d) / len(d))
    sig_mod.append(sum(d_mod) / len(d_mod))
    k_org.append(k_value(sum(d) / len(d), dis))
    k_mod.append(k_value(sum(d_mod) / len(d_mod), dis))
    # Distance: 1.2
    dis = 1.2
    d = [-31, -32, -33, -32, -33, -32, -32, -32, -34, -34, -36, -31, -32, -32, -33, -34, -33, -33, -33, -33, -34, -32, -33, -32, -33, -34, -33, -32, -34, -33, -33, -33, -34, -33]
    d.sort(reverse=True)
    d_mod = d[:len(d) // partition]
    data_org.extend(d)
    data_mod.extend(d_mod)
    for i in range(len(d)):
        x_org.append(1.2)
    for _ in range(len(d_mod)):
        x_mod.append(1.2)
    print(f"AVG {sum(d) / len(d):.2f} Distance : {dis}")
    print(f"AVG {sum(d_mod) / len(d_mod):.2f} Distance : {dis}")
    sig_org.append(sum(d) / len(d))
    sig_mod.append(sum(d_mod) / len(d_mod))
    k_org.append(k_value(sum(d) / len(d), dis))
    k_mod.append(k_value(sum(d_mod) / len(d_mod), dis))
    # 1.6
    dis = 1.6
    d = [-28, -28, -34, -28, -28, -28, -28, -26, -32, -28, -28, -28, -33, -28, -28, -28, -29, -28, -28, -28, -28, -28, -28, -28, -28, -28, -28, -28, -28, -28, -29, -29, -33, -28, -28, -28, -34, -26, -27, -33, -28, -28]
    d.sort(reverse=True)
    d_mod = d[:len(d) // partition]
    data_org.extend(d)
    data_mod.extend(d_mod)
    for i in range(len(d)):
        x_org.append(1.6)
    for _ in range(len(d_mod)):
        x_mod.append(1.6)
    print(f"AVG {sum(d) / len(d):.2f} Distance : {dis}")
    print(f"AVG {sum(d_mod) / len(d_mod):.2f} Distance : {dis}")
    sig_org.append(sum(d) / len(d))
    sig_mod.append(sum(d_mod) / len(d_mod))
    k_org.append(k_value(sum(d) / len(d), dis))
    k_mod.append(k_value(sum(d_mod) / len(d_mod), dis))
    # 2.0
    dis = 2.0
    d = [-39, -37, -38, -41, -37, -37, -39, -40, -40, -40, -39, -40, -38, -38, -39, -37, -36, -33, -36, -37, -39, -40, -40, -38, -40, -39, -41, -41, -39, -39, -40, -39, -35, -37, -38, -39, -41, -40, -40, -38, -38, -40, -42, -41]
    d.sort(reverse=True)
    d_mod = d[:len(d) // partition]
    data_org.extend(d)
    data_mod.extend(d_mod)
    for i in range(len(d)):
        x_org.append(2.0)
    for _ in range(len(d_mod)):
        x_mod.append(2.0)
    print(f"AVG {sum(d) / len(d):.2f} Distance : {dis}")
    print(f"AVG {sum(d_mod) / len(d_mod):.2f} Distance : {dis}")
    sig_org.append(sum(d) / len(d))
    sig_mod.append(sum(d_mod) / len(d_mod))
    k_org.append(k_value(sum(d) / len(d), dis))
    k_mod.append(k_value(sum(d_mod) / len(d_mod), dis))
    # 2.4
    dis = 2.4
    d = [-32, -35, -34, -34, -35, -34, -34, -32, -35, -29, -30, -32, -34, -32, -33, -33, -33, -34, -33, -35, -34, -34, -34, -34, -31, -33, -32, -34, -34, -34, -35, -35, -32, -34, -33, -30, -33, -33, -34, -35, -34, -34]
    d.sort(reverse=True)
    d_mod = d[:len(d) // partition]
    data_org.extend(d)
    data_mod.extend(d_mod)
    for i in range(len(d)):
        x_org.append(2.4)
    for _ in range(len(d_mod)):
        x_mod.append(2.4)
    print(f"AVG {sum(d) / len(d):.2f} Distance : {dis}")
    print(f"AVG {sum(d_mod) / len(d_mod):.2f} Distance : {dis}")
    sig_org.append(sum(d) / len(d))
    sig_mod.append(sum(d_mod) / len(d_mod))
    k_org.append(k_value(sum(d) / len(d), dis))
    k_mod.append(k_value(sum(d_mod) / len(d_mod), dis))

    # 3.0
    dis = 3.0
    d = [-41, -42, -42, -41, -41, -41, -41, -41, -40, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -41, -42, -41, -40, -40, -42, -43, -43, -44, -42, -43, -43, -44, -43, -44, -42]
    d.sort(reverse=True)
    d_mod = d[:len(d) // partition]
    data_org.extend(d)
    data_mod.extend(d_mod)
    for i in range(len(d)):
        x_org.append(3.0)
    for _ in range(len(d_mod)):
        x_mod.append(3.0)
    print(f"AVG {sum(d) / len(d):.2f} Distance : {dis}")
    print(f"AVG {sum(d_mod) / len(d_mod):.2f} Distance : {dis}")
    sig_org.append(sum(d) / len(d))
    sig_mod.append(sum(d_mod) / len(d_mod))
    k_org.append(k_value(sum(d) / len(d), dis))
    k_mod.append(k_value(sum(d_mod) / len(d_mod), dis))
    # 3.5
    dis = 3.5
    d = [-40, -40, -40, -40, -42, -40, -40, -40, -40, -42, -40, -42, -42, -42, -43, -43, -43, -43, -43, -43, -43, -43, -43, -43, -42, -42, -43, -43, -43, -43, -42, -42, -41, -42, -42, -42, -42, -40, -42, -38, -39, -38, -39, -37, -38, -41]
    d.sort(reverse=True)
    d_mod = d[:len(d) // partition]
    data_org.extend(d)
    data_mod.extend(d_mod)
    for i in range(len(d)):
        x_org.append(3.5)
    for _ in range(len(d_mod)):
        x_mod.append(3.5)
    print(f"AVG {sum(d) / len(d):.2f} Distance : {dis}")
    print(f"AVG {sum(d_mod) / len(d_mod):.2f} Distance : {dis}")
    sig_org.append(sum(d) / len(d))
    sig_mod.append(sum(d_mod) / len(d_mod))
    k_org.append(k_value(sum(d) / len(d), dis))
    k_mod.append(k_value(sum(d_mod) / len(d_mod), dis))

    print(sum(k_org) / len(k_org))
    print(sum(k_mod) / len(k_mod))
    dis_lst = [0.5, 0.85, 1.2, 1.6, 2.0, 2.4, 3.0, 3.5]
    
    t2 = np.arange(0.1, 4.0, 0.02)
    plt.figure(figsize=FIG_SIZE, dpi=DPI)
    plt.plot(t2, rssi_func(sum(k_org) / len(k_org), t2), label='Base + Free Space', linewidth=LINE_WIDTH)
    plt.plot(t2, rssi_func(sum(k_mod) / len(k_mod), t2), label='50% + Free Space', linewidth=LINE_WIDTH)
    plt.plot(t2, OLS_func(-22.6658, -28.7088, t2), label='Base + OLS', linewidth=LINE_WIDTH)
    plt.plot(t2, OLS_func(-22.7634, -27.6760, t2), label='50% + OLS', linewidth=LINE_WIDTH)
    plt.scatter(x=x_org, y=data_org, marker='>', label='Base', s=MARKER_SIZE)
    plt.scatter(x=x_mod, y=data_mod, marker='o', label='50%', s=MARKER_SIZE)
    plt.grid()
    plt.xlabel('Distance (m)', fontsize=LABEL_FONT_SIZE)
    plt.ylabel('RSSI (dbm)', fontsize=LABEL_FONT_SIZE)
    plt.xlim((0, 4))
    plt.legend(loc="best", fontsize=LEGEND_FONT_SIZE)
    plt.xticks(fontsize=TICKS_FONT_SIZE)
    plt.yticks(fontsize=TICKS_FONT_SIZE)
    plt.savefig('rssi_dis.png')
    plt.savefig('rssi_dis.pdf')
    
    

    x_org = np.log10(x_org)
    x_mod = np.log10(x_mod)
    x_org = sm.add_constant(x_org)
    results = sm.OLS(data_org, x_org).fit()
    print(results.summary())
    fi = open('./org.txt', 'w')
    fi.write(f"{results.summary()}")
    fi.close()
    x_mod = sm.add_constant(x_mod)
    results = sm.OLS(data_mod, x_mod).fit()
    print(results.summary())
    fi = open('./mod.txt', 'w')
    fi.write(f"{results.summary()}")
    fi.close()