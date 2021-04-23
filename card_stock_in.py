#coding:utf-8
import random


class Logger:
    # HEADER = '\033[95m'
    OKBRED = '\033[1;32;91m'
    # OKBLUE = '\033[1;32;94m'
    # OKGREEN = '\033[92m'
    # WARNING = '\033[93m'
    # FAIL = '\033[91m'
    BACKG_YELLOW = '\033[103m'
    ENDC = '\033[0m'

sim_type = input(Logger.BACKG_YELLOW+Logger.OKBRED+'请输入SIM类型：')

def file_name(a):
    sim_list={}
    with open (a,'r') as f:
        for line in f:
            line_imsi=line.strip()
            line_ic=line.strip()[-6:]
            stock='893520191030%s%s,%s,%s,%s,%s,%s,,,,'%(line_ic,random.randint(0,9),line_imsi,random.randint(1000,9999),random.randint(10000000,99999999),random.randint(10000000,99999999),sim_type)
            actual='893520191030%s%s,%s'%(line_ic,random.randint(0,9),line_imsi)
            sim_list.setdefault(stock,[]).append(actual)
    return sim_list



def write_stock(a,b):
    with open(b,'w') as w:
        w.write('ICCID,IMSI,PIN2,PUK1,PUK2,MODEL,MANUFACTURER,SUBTPE,PROFILE,PIN1'+'\n')
        for line_stock,line_actual in a.items():
            # print (line_stock)
            w.write(line_stock.strip()+'\n')

def write_actual(x,y):
    with open(y,'w') as w:
        w.write('ICCID,IMSI'+'\n')
        for line_stock,line_actual in x.items():
            # print (line_actual[0])
            w.write(line_actual[0].strip()+'\n')

print('执行结果在桌面的"stock_in.txt" 和 “stock_actual_in.txt” 中')

if __name__ =='__main__':
    a=file_name('1')
    b='C:/Users/hujl/Desktop/stock_in.txt'
    y='C:/Users/hujl/Desktop/stock_actual_in.txt'
    write_stock(a,b)
    write_actual(a,y)