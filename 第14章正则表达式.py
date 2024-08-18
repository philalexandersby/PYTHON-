#python中正则表达式的应用范围非常广泛，如实现数据挖掘、数据分析、网络爬虫、输入有效性验证等。 
#import re
#p1=r'\w+@zhijieketang\.com'
#p2=r'^\w+@zhijieketang\.com$'
#text="Tony's email is tony_guan588@zhjieketang.com"
#s=re.search(p1,text)
#print(s)
#x=re.search(p2,text)
#print(x)
#email="Tony_guan588@zhijieketang.com"
#y=re.search(p2,email)
#print(y)
#import re

#p1=r'\w+@163\.com'
#p2=r'^\w+@163\.com$'
#text="Theemai   lofsunboyangissuboyang@163.com"
#ans1=re.search(p1,text)
#ans2=re.search(p2,text)

#print(ans1)
#print(ans2)
#import re
#p1='[Jj]ava'
#m=re.search(p1,'I like java and python')
#print(m)
#import re
#p1=r'[Jj][Aa][vV][Aa]'
#print(re.search(p1,'JAVA'))
#import re
#a1=r'[^7687634576357456746]'
#print(re.search(a1,'sdfsdfdsfdsf'))
#import re
#print(re.search(r'[0-9a-zA-Z]+','4634SDF4D5F4D'))
#print(re.search(r'\D','54545'))
#print(re.search(r'\w+','sdhfsdldf46465465'))
#print(re.search(r'\d?','1s12dfd'))
#print(re.search(r'\d*','0a1313'))
#print(re.search(r'\d{8}',"q41341781"))
#print(re.search(r'\d{1,3}','1q2w3e4r5646'))
#print(re.search(r'\d{5,9}','qw4e6w4e5w464654646'))
#print(re.search(r'\d{5,9}?','qw4e6w4e5w464654646'))
#import re 
#p=r'(121){2}'
#m=re.search(p,'121121abcabc')
#print(m)
#print(m.group())
#print(m.group(1))
#p=r'(\d{3,4})-(\d{7,8})'
#m=re.search(p,'010-87654321')
#print(m)
#print(m.group())
#print(m.groups())
#import re
#p=r'(121){2}'
#print((re.search(p,'121121abcabc')).group())
#print((re.search(p,'121121abcabc')).group(1))
#print((re.search(p,'121121abcabc')).group(1))
#print((re.search(p,'121121abcabc')).groups())
#print(re.search(r'(\d{3,4}-\d{7,8})','198-01806179'))
#import re
#p=r'(?P<area_code>\d{3,4})-(?P<phone_code>\d{7,8})'
#m=re.search(p,'198-01806179')
#print(m)
#print(m.group(1))
#print(m.groups())
#print(m.group(2))
#print(m.group('area_code','phone_code'))
#p=r'(?P<area_code>d{3,4})-(?P<phone_code>\d{7,8})'
#import re
#p=r'<([\w+])>.*</([\w]+)>'
#m=re.search(p,'<a>abc</a>')
#print(m)
#m=re.search(p,'<a>abc</b>')
#print(m)
#import re
#s='img1.jpg,img2.jpg,img3.bmp'
#p=r'(\w+)(\.jpg)'
#l=r'\w+(?:\.jpg)'
#ans1=re.findall(p,s)
#ans2=re.findall(l,s)
#print(ans1)
#print(ans2)
#ans3=re.search(p,s)
#ans4=re.search(l,s)
#print(ans3.group(0))
#print(ans3.group(1))
#print(ans3.group(2))
#print(ans3.groups(0))
#print(ans3.groups(1))
#print(ans3.groups(2))
#import re 
#text1='sss _ sds is zhijieketang@163.com'
#text2='zhijieketang@163.com'
#p=r'\w+@163\.com'
#ans1=re.match(p,text1)
#ans2=re.match(p,text2)
#ans3=re.search(p,text1)
#ans4=re.search(p,text2)
#p2=r'(\w+)(@163\.com)'
#ans5=re.match(p2,text1)
#ans6=re.match(p2,text2)
#ans7=re.search(p2,text1)
#ans8=re.search(p2,text2)
#print(ans1,end='\n')
#print(ans2,end='\n')
#print(ans3,end='\n')
#print(ans4,end='\n')
#print(ans5,end='\n')
#print(ans6)
#print(ans7)
#print(ans8)
#import re
#text='i like Python and Java'
#p=r'[Jj]ava'
#ans1=re.findall(p,text)
#print(ans1)
#ans2=re.finditer(p,text)
#for m in ans2:
#    print(m)
#    print(m.group())
#import re
#text='AF12DF12DF2345DF46'
#p=r'\d+'
#ans1=re.split(p,text)
#print(ans1)
#ans2=re.split(p,text,1)
#print(ans2)
import re
p=r'\d+'
text='AD132134133MFGLKSDGJSL46443546'
ans1=re.sub(p,'牛',text)
print(ans1)
