#coding:utf-8


def imsi_deal():
    read_dic={}
    for line in range(int(270011999041961),int(270011999041999)):
        line_list=str(line).strip()[-3:-1]
        line_new=str(line).strip()[-3:]
        read_dic.setdefault(line_list, []).append(line_new)
    print(read_dic)
    return(read_dic)



if __name__=='__main__':
    imsi_deal()
