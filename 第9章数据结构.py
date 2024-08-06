# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 18:05:28 2024

@author: Administrator
"""
#索引操作
#a='hello'
#print(max(a))
#print(min(a))
#print(len(a))
#序列的加和乘
#a="hello"
#a+='world'
#print(a*3)
#序列分片
#a='hello'
#print(a[1:3])
#print(a[:3])
#print(a[1],a[0],a[-1],a[1:-1])
#print(a[::-1])
#元组
#a=(21,32,43,45)
#print(a)
#b=('hello','world')
#print(b)
#c=tuple([21,22])
#print(c)
#d=(21)
#type(d)
#a=('hello','world',1,2,3)
#print(a[:2])
#b,*c=a
#print(c)
#student_list=['张三','李四','王五']
#student_list.append('董六')
#print(student_list)
#student_list+=['刘备','关羽']
#print(student_list)
#student_list.extend([666])
#print(student_list)
#student_list.insert(2,'董卓')
#print(student_list)
#student_list[0]='诸葛亮'
#print(student_list)
#student_list.remove('诸葛亮')
#print(student_list)
#student_list.pop(2)
#print(student_list)
#student_list=['张三','李四','王五']
#student_list.reverse()

#b=student_list.copy()
#print(student_list)
#print(b)
#3c=b.clear(0)
#print(c)
#n_list=[]
#for x in range(10):
#    if x % 2 == 0:
#     n_list.append(x**2)
#print(n_list)
#n_list=[x for x in range (10) if x%2==0 if x %5==0]
#print(n_list)
#a={'张三','李四','王五','王五'}
#a.add('董六')
#print(a) 
#a.discard('张三')
#print(a)
#a.clear()
#print(a)
#student_set=('张三','李四','王五')
#for item in student_set:
 #   print('-----------')
  #  for i, item in enumerate (student_set):
   #     print('{0}-{1}'.format(i,item))
#student_set = ('张三', '李四', '王五')
#print('-----------')
#for i, item in enumerate(student_set):
 #   print('{0}-{1}'.format(i, item))
#student_set=frozenset({'张三','李四','王五'})
#print(student_set)
#c=type(student_set)
#print(c)
#a=(21,32,43,45)
#seta=frozenset(a)
#print(seta)
#input_list=[2,2,2,2,2,4,9,8,7,4,5,2,3,6,9,9,9,9,63]
#n_list=[x**2 for x in input_list]
#print(n_list)
#n_set={x**2 for x in input_list}
#print(n_set)
#字典的几种描写形式
#dict1={101:'张三',102:'李四',103:'王五'}
#a=len(dict1)
#print(dict1,a)
#dict2=({101:'zhagnsan',102:'lisi',103:'wangwu'})
#print(dict2)
#dict3=([(101:'zhangsan'),(102:'lisi'),(103:'wangwu')])
#print(dict3)
#t1={101:'zhangsna'};t2={102:'lisi'};t3={103:'wangwu'};
#t=(t1,t2,t3)
#print(t)
dict2={111:'zhangsan',112:'lisi',113:'wangwu'}
new_value=dict2.pop(111) 
#print(new_value)
a=dict2.values()
print('---遍历键----')
for student_id in dict2.keys():
    print('学号：'+str(student_id))
                      