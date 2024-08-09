#def retangle_area (width,length):
#    area=width*length
#    return area
#r_area=retangle_area(320,110)
#print('长方形的面积={0}'.format(r_area))
#def retangle_area (width,height):
#    area=width*height
#    print("{0}={1}*{2}".format(area,width,height))
    
    
#retangle_area(320, 630)
#def make_coffee(name='卡布奇诺'):
#    print('制作一杯{0}'.format(name))
    
#make_coffee()
#make_coffee('拿铁')
#def sum(*numbers,multiple=1):
#    total=0
#    for number in numbers:
#        total += number
#    return total*multiple
    
#print(sum(320,12,980))
#print(sum(30,80,multiple=300))
#double_tuple=(30,12,70)  
#print(sum(30,20,*double_tuple))
#def show_info(sep=':',**info):
#    print('----info-----')
#    for key,value in info.items():
#        print('{0} {2} {1}'.format(key,value,sep))
        
#show_info('->',name='Tony',age=18,sex=True)
#def show_info (sep=':',**info):
#    print('----info----')
#    for key,value in info.items():
#        print('{0} {2} {1}'.format(key,value,sep))
        
#show_info('->',name='Tony',age=18,sex='男')
#def show_info(sep=':',**info):
#    for key,value in info.items():
#        print('{0} {1} {2}'.format(key,sep,value))
#    return
#result= show_info('->',name='Tony',age=18,sex=True)
#print(result)
#def sum(*numbers,multiple=1):
#    if len(numbers)==0:
#        return
#    total=0
#    for number in numbers:
#        total+=number
#    return total*multiple
#print(sum(30,80))
#print(sum(multiple=2))
#x=20
#def value():
#    print('函数内变量为{0}'.format(x))
    
#a=value()
#print('函数外变量为{0}'.format(x))
#x=20
#def value():
#    x=10
#    print('函数内部的变量为{0}'.format(x))
#value()    
#print('函数外部的变量为{0}'.format(x))
#x=10
#def value ():
#    global x
#    x=20
#    print('函数内变量为{0}'.format(x))
#print('函数外变量为{0}'.format(x))
#value()
#def square (num):
#    n_list=[]
#    for i in range (1,num+1):
#        n_list.append(i*i)
#        
#    return n_list
#for i in square(5):
#    print (i,end='')
#def square (num):
#    n_list=[]

#    for i in range (1,num+1):
#     n_list.append(i*i)
#    return n_list
#results=square(5)
#print(results)
#def calculate (n1,n2,opr):
#    multiple=2
#    def add(a,b):
#        return (a+b)*multiple
#    def sub (a,b):
#        return(a-b)*multiple
#    if opr=='+':
#        return add(n1,n2)
#    else:
#        return sub(n1,n2)
#print(calculate(10,5,'+'))
#def calculate(n1,n2,opr):
#    multiple=2
#    def add(a,b):
#        return ((a+b)*multiple)
#    def sub(a,b):
#        return((a-b)*multiple)
#    if opr=='+':
#        return add(n1,n2)
#    else:
#        return sub(n1,n2)
#print(calculate(10,6,'-'))
#def calculate (n1,n2,opr):
#    multiple=2
#    def add(a,b):
#        return((a+b)*multiple)
#    def sub(a,b):
#        return((a-b)*multiple)
#    if opr=='+':
#        return(add(n1,n2))
#    else:
#        return(sub(n1,n2))
    
#print(calculate(11646161,7676746,'-'))
#def calculate (opr):
#    multiple=3
#    def add(a,b):
#        return((a+b)*multiple)
#    def sub(a,b):
#        return((a-b)*multiple)
#    if opr=='+':
#     return add
#    else:
#     return sub
#f1=calculate('+')
#f2=calculate('-')
#print('10+5={0}'.format(f1(10,5)))
#print('10-5={0}'.format(f2(10,5)))
#def calculate (opr):
#    multiple=1
#    if opr=='+':
#     return lambda a,b:(a+b)
#    else:
#     return lambda a,b:(a-b)
 
#f1=calculate('+')
#f2=calculate('-')
#print('10+5={0}'.format(f1(10,5)))
#print('10-5={0}'.format(f2(10,5)))
#users=['Tony','Tom','Danney']
#users_fieter=filter(lambda u:u.startswith('T'),users)
#print(list(users_fieter))
#number_list=range(1,99)
#number_list2=filter(lambda u:u%5==0,number_list)
#print(number_list2)
#print(list(number_list2))
#users_list=['Tony','DasASDFASF','SDFSDFSD','DFSDAFSDAasdfasdfsadf']
#transfomer_list=map(lambda t:t.lower(),users_list)
#print(transfomer_list)
#print(list(transfomer_list))
#users_list=['sldfhsodfFASOFHASODFHAS','TDHFKASDFHS','jaslfjalsdjflsdTf']
#transformer=map(lambda t:t.lower(),filter(lambda u:u.startswith('T'),users_list))
# print(list(transformer))
#from functools import reduce
#a=(1,2,3,4)
#a_reduce=reduce(lambda acc,i:acc+i,a)
#print(a_reduce)
#from functools import reduce
#a=(1,2,3,45,89,-89,1/2,437435435)
#a_reduce=reduce(lambda u,t:u*t,a)
#print(a_reduce)

   