#coding:utf-8

def get_attr():
    linedic={}
    with open('2','r',encoding='utf-8') as ra:
        for line in ra:
            line_list=line.strip().split('=')
            linedic[line_list[0]]=line_list[1]
            # linedic.setdefault(line_list[0],line_list[1])
    # print(linedic)
    with open('b','r',encoding='utf-8') as rb:
        for line in rb:
            line_b=line.strip().split('=')
            if line_b[0].strip()!='{' and line_b[0].strip()!='}':
                if line_b[0][:2].strip()!='17':
                    expl=linedic.get(line_b[0],'/**/')
                    event_attr=line.strip()+expl
                else:
                    expl='/*项目化的属性*/'
                    event_attr = line.strip()+expl
                event_attr=event_attr.replace(',','')
                print(event_attr.strip())

if __name__=='__main__':
    get_attr()
