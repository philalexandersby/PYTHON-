# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 13:06:53 2024

@author: Administrator
"""
#class Anminal (object):
#    def __init__ (self,sex,age,weight):
#        self.sex=sex

#        self.age=age
#        self.weight=weight
        
#anminal=Anminal('男性',18,'60 kg')
#print(anminal.sex)
#class Animal(object):  # 注意这里类名应为 Animal，而不是 Anminal
#    def __init__(self, sex, age, weight):  # 正确的构造函数名是 __init__
#        self.sex = sex
#        self.age = age
#        self.weight = weight

# 创建实例
#animal = Animal('男性', 18, '60 kg')  # 确保类名拼写正确

# 访问实例的属性
#print(animal.sex)  # 应该使用实例名访问属性，而不是类名
#class account:
#    interest_rate=0.0668
#    def __init__(self,owner,amount):
#        self.owner=owner
#        self.amount=amount
        
#Account=account(' Tony','   USDT 18000')
#print('账户拥有者{0}'.format(Account.owner))
#print('账户余额{0}'.format(Account.amount))
#print('银行利率   {0}'.format(account.interest_rate))        
#print('银行利率{0}'.format(account.interest_rate))
#print('银行利率{0}'.format(Account.interest_rate))
#print('所有示例变量{0}'.format(Account.__dict__)) 
#class animal :
#    def __init__(self,sex,age,weight=0.0):
#        self.sex=sex
#        self.age=age
#        self.weight=weight
        
        
#a1=animal(1,20,10.0)
#a2=animal(age=5,sex=1,weight=50)
#a3=animal(age=6,sex=0,weight=7)
 
#print('a1 年龄：{0}'.format(a1.age))
#print('a2 体重：{0}'.format(a2.weight))
#print('a3 性别：{0}'.format('雌性'if a3.sex==0 else '雌性'))
#class Animal(object):
#    def __init__(self,sex,age,weight):
#        self.sex=sex
#        self.age=age
#        self.weight=weight
        
#    def eat(self):
#        self.weight+=0.05
#        print('eat...')
        
#    def run(self):
#        self.weight-=0.01
#        print('run...')
        
        
#a1=Animal(2,0,10.0)
#print('a1 体重：{0:0.2f}'.format(a1.weight))
#a1.eat()
#print('a1 体重：{0:0.2f}'.format(a1.weight))
#a1.run()
#print('a1 体重：{0:0.2f}'.format(a1.weight))
#class animal(object):
#    def __init__(self,age,sex,weight):
#        self.age=age
#        self.sex=sex
#        self.weight=weight
        
#    def eat(self):
#            self.weight+=0.05
#            print('吃了')
            
#    def run(self):
#            self.weight-=0.07
#            print('运动了')
            
#a1=animal(10,'男性',60)
#print('a1 体重：{0:0.2f}'.format(a1.weight))
#a1.eat()
#print('a1 体重：{0:0.2f}'.format(a1.weight))
#a1.run()
#print('a1 体重：{0:0.2f}'.format(a1.weight))
#class Account:
#    interest_rate=0.0668
#    def __init__(self,owner,amount):
#        self.owner=owner
#        self.amount=amount
        
#        @classmethod
#        def interest_by (cls,amt):
#            return cls.interest_rate*amt
#        interest=Account.interest_by(12000.0)
#        print('计算利率：{0：0.4f}'.format(interest))
#class Account (object):
# interest_rate=0.068
# def __init__ (self,owner,account):
#    self.owner=owner
#    self.account=account
    
# @classmethod
# def interest_by(cls,amt):
#    return cls.interest_rate*amt

#a1=Account.interest_by(1200000)
#print('计算利息：{0}'.format(a1))
#class Account:
#    interest_rate=0.068
#    def __init__(self,amount,owner):
#        self.amount=amount
#        self.owner=owner
        
#    @classmethod
#    def interest_by(cls,amt):
#        return cls.interest_rate*amt
    
#    @staticmethod
#    def interest_with(amt):
#        return Account.interest_by(amt)
    
#interest1=Account.interest_by(12000)
#print('计算利息：{0:4f}'.format(interest1))
#interest2=Account.interest_by(45121)
#print('计算利息：{0:4f}'.format(interest2))
#class Account(object):
#    interest_rate=0.068
#    def __init__(self,amount,owner):
#        self.owner=owner
#        self.amount=amount
#    @classmethod    
#    def interest_by(cls,amt):
#        return cls.interest_rate*amt
#    @staticmethod
#    def interest_with(amt):
#        return Account.interest_by(amt)
    
#a1=Account.interest_by(120000)
#print('计算利息：{0:0.4f}'.format(a1))
#a2=Account.interest_with(34341354)
#print('计算利息：{0:0.4f}'.format(a2))
#class Animal (object):
#    def __init__(self,sex,age,weight=0):
#        self.sex=sex
#        self.age=age
#        self.__weight=weight
        
#    def eat(self):
#        self.__weight+=0.3
#        print('吃了')
#    def run(self):
#        self.__weight-=0.01
#        print('运动了')
        
#a1=Animal(0,12,1000)
#a1.eat()
#print('饭后体重为：{0}'.format(a1.weight))
#a1.run()
#print('运动后体重为：{0}'.format(a1.weight))
#class Animal (object):
#    def __init__(self,sex,weight,age):
#        self.age=age
#        self.weight=weight
#        self.sex=sex
        
#    def weight_set(self,weight):
#        self.weight=weight
        
#    def weight_get(self):
#        return self.weight
    
#A1=Animal('男性',80,16)
#print('体重为：{0:2f}'.format(A1.weight))
#A1.weight_set(1234.1344)
#print('体重为：{0:2f}'.format(A1.weight))        
#class person:
#    def __init__ (self,name,age):
#        self.name=name
#        self.age=age
        
#    def info(self):
#        templete='Person [name={0},age={1}]'
#        a=templete.format(self.name,self.age)
#        return a
#b=person('Tom',66)
#print('姓名为：{0}'.format(b.name))
#print('年龄为：{0}'.format(b.age))           
#class personal(object):
#    def __init__ (self,sex,name,school,age):
#        self.age=age
#        self.name=name
#        self.school=school        
#        self.sex=sex
#    def info(self):
#        templete='学生姓名为：{0}，学生年龄为{1}，学生性别为{2}，学生学校为{3}'
#        s=templete.format(self.name,self.age,self.sex,self.school)
#        return s
#a=personal('男性','Tom','**大学',16)
#print(a.info())
#class personal(object):
#    def __init__(self,age,sex):
#        self.age=age
#        self.sex=sex
        
#class student(personal):
#    def __init__(self,name,school,age,sex):
#        super().__init__(age,sex)
#        self.name=name
#        self.school=school
#    def info(self):
#        templete='学生姓名为：{0}，学生学校为：{1}，学生性别为：{2}，学生年龄为：{3}'
#        s=templete.format(self.name,self.school,self.sex,self.age)
#        return s
#a=student('Tom','**中学','男','16')
#print(a.info())
#class Figure (object):
#    def draw (self):
#        print('绘制Figure....')
        
#class Ellipse(Figure):
#    def draw (self):
#        print('绘制Ellipse....')
        
#class Triangle(Figure):
#    def draw(self):
#        print('绘制Triangle....')
    
#f1=Figure()
#f1.draw()
#f2=Ellipse()
#f2.draw()
#f3=Triangle()
#f3.draw()
#print(isinstance(f1,Triangle))
#print(isinstance(f2,Triangle))
#print(isinstance(f3,Triangle))
#print(isinstance(f2,Figure))
#print(isinstance(f3,Figure))
#class Animal(object):
#    def run(self):
#        print('动物跑....')
#class Dog(Animal):
#    def run(self):
#        print('狗狗跑....')
#class Car:
#    def run(self):
#        print('汽车跑....')
#def go(animal):
#    animal.run()
    
#go(Animal())
#go(Dog())
#go(Car())
#class Animal(object):
#    def run (self):
#        print('动物跑....')
#class Dog(Animal):
#    def run(self):
#        print('狗狗跑....')
#class Car:
#    def run(self):
#        print('汽车跑....')
#def go (animal):
#    animal.run()
#go(Animal())
#go(Dog())
#go(Car())
#class Animal(object):
#    def run (self):
#        print('动物跑....')
        
#class Dog(Animal):
#    def run(self):
#        print('狗狗跑....')
        
#class Car(object):
#    def run(self):
#        print('汽车跑....')
        
#def go(animal):
#    animal.run()
    
#print(go(Animal()))        
#class Animal(object):
#    def run(self):
#        print('动物跑')
#class Dog(Animal):
#    def run (self):
#        print('狗狗跑')
#class Car(object):
#    def run(self):
#        print('汽车跑')

#def go(animal):
#    animal.run()
#print(go(Animal()))
#print(go(Dog()))
#print(go(Car()))    
#class person(object):
#    def __init__(self,name,age):
#        self.age=age
#        self.name=name
        
#    def __str__(self):
#        template='Person [{0},{1}]'
#        s=template.format(self.age,self.name)
#        return s
    
#Person=person(16,'Tony')
#print(Person)
#class person(object):
#    def __init__(self,age,name):
#        self.age=age
#        self.name=name
#    def __str__(self):
#        template='个人信息 [{0},{1}]'
#        return template.format(self.age,self.name)
#    def __eq__ (self,other) :
#        if self.name==other.name and self.age==other.age:
#            return True
#        else:
#            return False
        
#p1=person(16,'TONY')
#p2=person(16,'TONY')
#p3=person(17,'TONY')
#print(p1==p2)
#print(p1==p3)
#print(p2==p3)
import enum
class WeekDays(enum.Enum):
    MONDAY=10
    TUESDAY=20
    WEDNESDAY=70
    THURSDAY=40
    FRIDAY=40
    SATURSDAY=60
    SUNDAY=30
S=WeekDays.MONDAY    
print(S)
print(S.value)
print(S.name)
           
        
        
        
    
    
    
        


    
       
        
        
        
    
    
    



   