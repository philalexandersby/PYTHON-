# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:54:37 2024

@author: Administrator
"""

#import csv
#with open(r'C:\Users\Administrator\Desktop\S1-1.csv','r',encoding='gbk') as rf:
#    reader = csv.reader(rf,dialect=csv.excel)
#    for row in reader:
#        print('|'.join(row))
#import pandas as pd

# 读取 Excel 文件
#df = pd.read_excel(r'C:\Users\Administrator\Desktop\S1-1.xlsx')

# 保存为 CSV 文件
#df.to_csv(r'C:\Users\Administrator\Desktop\S1-1.csv', index=False, encoding='utf-8')
#import csv
#with open (r'C:\Users\Administrator\Desktop\S1-1.csv','r',encoding='gbk') as rf:
#    reader=csv.reader(rf,dialect=csv.excel)
#    for row in reader:
#        print('|'.join(row))
#import csv
#with open (r'C:\Users\Administrator\Desktop\S1-1.csv','r',encoding='gbk') as rf:
#     reader=csv.reader(rf,dialect=csv.excel)
#     for row in reader:
#          print('|'.join(row))
#import csv
#with open(r'C:\Users\Administrator\Desktop\S1-1.csv','r',encoding='gbk') as rf:
#    reader=csv.reader(rf,dialect=csv.excel)
#    for row in reader:
#        print('|'.join(row))
#import csv
#with open (r'C:\Users\Administrator\Desktop\S1-1.csv','r',encoding='gbk') as rf:
#    reader=csv.reader(rf,dialect=csv.excel)
#    for row in reader:
#        print('|'.join(row))
#import csv
#with open (r'C:\Users\Administrator\Desktop\S1-1.csv','r',encoding='gbk') as rf:
# reader=csv.reader(rf,dialect=csv.excel)
# for row in reader:
#     print('|'.join(row))

#import csv
#with open (r'C:\Users\Administrator\Desktop\S1-1.csv','r',encoding='gbk') as rf:
# reader=csv.reader(rf,dialect=csv.excel)
# for row in reader:
#     print('|'.join(row))
#import csv
#with open (r'C:\Users\Administrator\Desktop\S1-1.csv','r',encoding='gbk') as rf:
#    reader=csv.reader(rf)
#    with open(r'C:\Users\Administrator\Desktop\S1-1.csv','w',newline='',encoding='gbk') as wf:
#        writer=csv.writer(wf,delimiter='\t')
#        for row in reader:
            #print('|'.join(row))
#            writer.writerow(row)
#            print('/'.join(row))
#import csv
#data=[
#     ['name','age','Location'],
#     ['Alice','18','New York'],
#     ['Tom','23','Los Angeles']
#      ]
#with open (r'C:\Users\Administrator\Desktop\666.csv','w') as file:
#    writer=csv.writer(file)
#    for row in data:
#        writer.writerow(row)
        
#with open (r'C:\Users\Administrator\Desktop\666.csv','r') as rf:
#    reader=csv.reader(rf)
#    for row in reader:
#        print(row)
#import csv
#data=[
#      ['Name','Age','Location'],
#      ['Alice','18','New York'],
#      ['Tom','89','Los Angelos']
#      ]
#with open (r'C:\Users\Administrator\Desktop\777.csv','w') as file1:
#    writer=csv.writer(file1)
#    for row in data:
#        writer.writerow(row)
#with open (r'C:\Users\Administrator\Desktop\666.csv','r') as file2:
#    reader=csv.reader(file2)
#    for row in file2:
#        print(row)
#import xml.etree.ElementTree as ET
#tree= ET.parse(r'C:\Users\Administrator\Desktop\my_note.xml')
#print(type(tree))
#root=tree.getroot()
#print(type(root))
#print(root.tag)
#for index,child in enumerate(root):
#    print('第{0}个{1}元素，属性：{2}'.format(index,child.tag,child.attrib))
#    for i,child_child in enumerate(child):
#        print('标签：{0}，内容：{1}'.format(child_child.tag,child_child.text))
#import xml.etree.ElementTree as ET
#tree=ET.parse('data/Notes.xml')
#root=tree.getroot()
#node=root.find('./Note')
#print(node.tag,node.attrib)
#node=root.find('./Note/CDate')
#print(node.text)
#node=root.find('./Note/CDate/..')
#print(node.tag,node.attrib)
#node=root.find('.//CDate')
#print(node.text)

#node=root.find('./Note[@id]')
#print(node.tag,node.attrib)

#node=root.find("./Note[@id='2']")
#print(node.tag,node.attrib)

#node=root.find("./Note[2]")
#print=(node.tag,node.attrib)

#node=root.find("./Note[last()]")
#print(node.tag,node.attrib)

#node=root.find("./Note[last()-2]")
#print(node.tag,node.attrib)
#import json 
#py_dict={'name':'Tony','age':'30','sex':True}
#py_list={1,3}
#py_tuple={'A','B','C'}
#py_dict['a']=py_list
#py_dict['b']=py_tuple
#print(py_dict)
#print(type(py_dict))


#json_obj=json.dumps(py_dict)
#print(json_obj)
#print(type(json_obj))

    #json_obj=json.dumps(py_dict,indent=4)
    #print(json_obj)
    
    
    #with open('data/datal.json','w') as f:
    #    json.dump(py_dict,f)
        
    #with open('data/data2.json','w') as f:
    #    json.dump(py_dict,f,indent=4)
#import json
#py_dict={'name':'Tony','Age':'18','Location':'Losangle'}
#py_list=[1,3]
#py_tuple=['A','B','C']
#py_dict['a']=py_list
#py_dict['b']=py_tuple
#json_obj=json.dumps(py_dict,indent=6)
#print(json_obj)
#print(type(json_obj))
#import json
#json_obj=r'{"name":"tony","sex":true,"a":[1,3],"b":["A","B","C"]}'
#py_dict=json.loads(json_obj)
#print(type(py_dict))
#print(py_dict['name'])

#print(py_dict['sex'])
#py_lista=py_dict['a']
#print(py_lista)
#py_listb=py_dict['b']
#print(py_listb)
#with open(r'C:\Users\Administrator\Desktop\6.json','r') as f:
#    data=json.load(f)
#    print(data)
#    print(type(data))

        
    