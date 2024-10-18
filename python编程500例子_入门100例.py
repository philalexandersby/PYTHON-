#import pymysql
#print('666')
#import pymysql



#connection=pymysql.connect(host='localhost',
#                           user='root',
#                           password='648028480',
#                           database='mydb',
#                           charset='utf8')
#CREAT DATABASE IF NOT EXISTS MyDB;
#use MyDB;
#CREATE TABLE IF NOT EXISTS user(
#    name varchar(20),
#    userid int,
#    PRIMARY KEY (usrid);
#    INSERT INTO user VALUES('Tom',1);
#    INSERT INTO user VALUES('Ben',2);
#    select name, userid from user where userid >?order by userid
#    select max (userid) from user
#    )
#class Solution:
#    def reverseInteger(self,number):
#        h=int(number/100)
#        t=int(number%100/10)
#        z=int(number%10)
#        return (100*z+10*t+h)
#if __name__=='__main__':
#    solution= Solution()
#    num= 123
#    ans=solution.reverseInteger(num)
#    print("输入：",num)
#    print("输出：",ans)
#问题描述：反转一个三位数字
#问题示例：输入103，输出301
#def reverteger(number):
#    h=int(number/100)
#    z=int(number/10%10)
#    t=int(number%10)
#    return(h+z*10+t*100)
#print(reverteger(456))
#问题描述：合并两个升序的整数数组A和B，形成一个新的数组，新数组也要有序。
#问题示例：输入A=[1],B=[1] 输出：[1,1] 输入A=[1,2,3,4],B=[2,4,5,6] 输出[1,2,2,3,4,4,5,6]
#class Solution:
#    def mergeSortedArry(self,A,B):
#        i,j=0,0
#        C=[]
#        while i<len(A) and j<len(B):
#            if A[i]<B[j]:
#                C.append(A[i])
#                i+=1
#            else:
#                C.append(B[j])
#                j+=1
#        while i<len(A):
#            C.append(A[i])
#            i+=1
#        while j<len(B):
#            C.append(B[j])
#            j+=1
#        return C
#if __name__=='__main__':
#    A=[1,4]
#    B=[1,2,3]
#    D=[1,2,3,4]
#    E=[2,4,5,6]
#    solution=Solution()
#    print("输入：",A,"",B)
#    print("输出：",solution.mergeSortedArry(A,B))
#    print("输入：",D,"",E)
#    print("输出：",solution.mergeSortedArry(D,E))
#def hanshu(A,B):
#    i,j=0,0
#    C=[]
#    while i<len(A) and j<len(B):
#        if A[i] < B[j]:
#            C.append(A[i])
#            i+=1
#        else:
#            B[j] < A[i]
#            C.append(B[j])
#            j+=1
#    while i<len(A):
#            C.append(A[i])
#            i+=1
#    while j<len(B):
#            C.append(B[j])
#            j+=1
#    return C
#print(hanshu(A=[1,2,3,5,9,8],B=[1,2,3,5,9,12,78]))            
#def hanshu (s,offset):
#    if len(s) > 0:
#        offset = offset % len(s)
#        temp = (s+s)[len(s)-offset:2*len(s)-offset]
#        for i in range(len(temp)):
#            s[i] = temp[i]
#def hanshu(A,offset):
#    offset=offset%len(A)
#    temp=(A+A)[len(A)-offset:2*len(A)-offset]
#    for i in range(len(temp)):
#        A[i]=temp[i]
#    return A
#print(hanshu(A=[4,4,56,45,4,54,65,46,64,67,89,4,],offset=6))
#def hanshu (nums):
#    score={}
#    for i in range(len(nums)):
#        score[nums[i]]=i
#    sortedScore = sorted(nums,reverse=True)
#    answer = [0]*len(nums)
#    for i in range(len(sortedScore)):
#        res = str(i+1)
#        if i== 0:
#            res='金牌'
#        if i==1:
#            res='银牌'
#        if i==2:
#            res='铜牌'
#        answer[score[sortedScore[i]]]=res
#        return answer 
#def hanshu (nums):
#    score={}
#    for i in range(len(nums)):
#        score[nums[i]]=i

#    sortedScore=sorted(nums,reverse=True)
#    answer=[0]*len(nums)
#    for i in range(len(sortedScore)):
#        res=str(i)
#        if i==0:
#            res='金牌'
#        elif i==1:
#            res='银牌'
#        elif i==2:
#            res='铜牌'
#        answer[score[sortedScore[i]]]=res
#    return answer
#print(hanshu(nums=[1,2,3,4,5,88,9]))
#def hanshu(nums,target):
#    return nums.index(target) if target in nums else-1       
#def hanshu (nums,target):
#    return nums.index(target) if target in nums else -1
# print(hanshu(nums=[1,4,64,6,46,4,64,6,4,6],target=64))               
#def hsnhu(nums1,nums2):
#    answer={}
#    stack={}
#    for x in nums2:
#        while stack and stack[-1]<x:
#            answer[stack[-1]] = x
#            del stack[-1]
#            stack.append(x)
#    for x in stack:
#        answer[x] = -1
#    return [answer[x] for x in nums1]
#def hanshu(nums1,nums2):
#    answer={}
#    stack=[]
#    for x in nums2:
#        while stack and stack[-1] <x:
#            answer[stack[-1]]=x
#            del stack[-1]
#        stack.append(x)
#    for x in stack:
#        answer[x]=-1
#    
#    return [answer[x] for x in nums1]
#
#print(hanshu(nums1=[7,97,9879,87],nums2=[979,79,7,97,9879,87,9,7,9,79]))
#def hanshu (s):
#    res=0
#    for i  in range(len(s)):
#        if s[i] !='' and (i==0 or s[i-1]==''):
#            res+=1
#    return res
#print(hanshu(s='dfsdf s sdf sdf sdfjsdfsdf,sf,sdf,sdf,sddfasdf sd asf s'))
#def hanshu(s):
#    res = 0
#    in_non_empty = False  # 用于标记当前是否在一个非空子串中
#    
#    for i in range(len(s)):
#        if s[i] != ' ':  # 如果当前字符非空（不为空格）#
#            if not in_non_empty:  # 如果之前没有在非空子串中
#                res += 1  # 增加计数
#                in_non_empty = True  # 现在进入了一个非空子串
#        else:
#            in_non_empty = False  # 当前字符为空格，退出非空子串
    
#    return res

#print(hanshu(s='dfsdf s sdf sdf sdfjsdfsdf,sf,sdf,sdf,sddfasdf sd asf s'))
#def hanshu (ransomNote,magazine):
#    arr=[0]*26
#    for c in magazine:
#        arr[ord(c)-ord('a')]+=1
#    for c in ransomNote:
#        arr[ord(c)-ord('a')]-=1
#        if arr[ord(c)-ord('a')]<0:
#            return False
#    return True
#def hanshu (nums1,nums2):
#    arr=[0]*26
#    for i in nums2:
#        arr[ord(i)-ord('a')]+=1
#    for i in nums1:
#        arr[ord(i)-ord('a')]-=1
#        if arr[ord(i)-ord('a')]<0:
#            return False
#    return True
# print(hanshu(nums1='sdfasfsadfsf',nums2='sdfsfsdfasf'))
#def hanshu(a):
#    ans=[0,0]
#    for i in a:
#        ans[0]=ans[0]^i
#    c=1
#    while c&ans[0]!=c:
#        c=c<<1
#    for i in a:
#        if i&c==c:
#            ans[1]=ans[1]^i
#    ans[0]=ans[0]^ans[1]
#    return ans
#def hanshu (nums1,nums2):
#    if len(nums1)!=len(nums2):
#        return -1
#    else:
#        c=0
#        for i in range (len(nums1)):
#            c+=nums1[i]*nums2[i]
#        return c
#print(hanshu(nums1=[1,2,3],nums2=[4,5,6]))
#import beautifulsoup4
#print(0)
#from bs4 import BeautifulSoup

#print("BeautifulSoup imported successfully")
#import requests
#from bs4 import BeautifulSoup
#import pandas as pd
#import time

#def get_journal_info(journal_title):
#    url = 'https://www.letpub.com.cn/index.php?page=journalapp'
#    headers = {'User-Agent': 'Mozilla/5.0'}
#    params = {'searchname': journal_title, 'view': 'search', 'fieldtag': '0', 'sort': 'realtime'}#

#    response = requests.get(url, headers=headers, params=params)
#    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract journal information
#    info = {}
#    try:
#        table = soup.find('table', {'class': 'table_yjfx'})
#        rows = table.find_all('tr')

        # Real-time Impact Factor
#        info['实时影响因子'] = rows[1].find_all('td')[1].text.strip()
#        # Review Speed
 #       info['平均审稿速度'] = rows[4].find_all('td')[1].text.strip()
        # Acceptance Rate
  #      info['平均录用比例'] = rows[5].find_all('td')[1].text.strip()
  #  except Exception as e:
  #      print(f"Error fetching data for {journal_title}: {e}")
  #      info['实时影响因子'] = 'N/A'
  #      info['平均审稿速度'] = 'N/A'
  #      info['平均录用比例'] = 'N/A'

   # return info

# Load the Excel file and read the journal titles
#file_path = r'C:\Users\Administrator\Desktop\refine.xlsx'
#df = pd.read_excel(file_path)

# Create a list to store the results
#results = []

# Iterate over each journal title in the DataFrame
#for title in df['出版物标题']:
#    print(f"Fetching data for: {title}")
#    journal_info = get_journal_info(title)
#    journal_info['出版物标题'] = title
#    results.append(journal_info)
#    
    # Pause to avoid overloading the server
#    time.sleep(1)

# Create a new DataFrame from the results
#results_df = pd.DataFrame(results)

# Save the results to a new CSV file
#results_df.to_csv('journal_info.csv', index=False, encoding='utf-8-sig')

#print("Data successfully saved to journal_info.csv")
#import requests
#from bs4 import BeautifulSoup
#import pandas as pd
#import time
#from requests.adapters import HTTPAdapter
#from requests.packages.urllib3.util.retry import Retry

#def get_journal_info(journal_title):
#    url = 'https://www.letpub.com.cn/index.php?page=journalapp'
#    headers = {'User-Agent': 'Mozilla/5.0'}
#    params = {'searchname': journal_title, 'view': 'search', 'fieldtag': '0', 'sort': 'realtime'}

#    session = requests.Session()
#    retry = Retry(total=5, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
#    adapter = HTTPAdapter(max_retries=retry)
#    session.mount('http://', adapter)
#    session.mount('https://', adapter)

#    try:
#        response = session.get(url, headers=headers, params=params, timeout=10)
#        response.raise_for_status()
#        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract journal information
 #       info = {}
 #       table = soup.find('table', {'class': 'table_yjfx'})
 #       rows = table.find_all('tr')

        #info['实时影响因子'] = rows[1].find_all('td')[1].text.strip()
        #info['平均审稿速度'] = rows[4].find_all('td')[1].text.strip()
        #info['平均录用比例'] = rows[5].find_all('td')[1].text.strip()
        
    #except requests.exceptions.RequestException as e:
    #    print(f"Error fetching data for {journal_title}: {e}")
    #    info['实时影响因子'] = 'N/A'
    #    info['平均审稿速度'] = 'N/A'
    #    info['平均录用比例'] = 'N/A'

    #return info

# Load the Excel file and read the journal titles
#file_path = r'C:\Users\Administrator\Desktop\refine.xlsx'
#df = pd.read_excel(file_path)

# Specify the output CSV file path
#output_file_path = r'C:\Users\Administrator\Desktop\结果.csv'

# Open the CSV file in append mode, and write the header if the file is empty
#with open(output_file_path, 'w', encoding='utf-8-sig', newline='') as f:
    # Write the header
#    f.write('出版物标题,实时影响因子,平均审稿速度,平均录用比例\n')

# Iterate over each journal title in the DataFrame
#for title in df['出版物标题']:
#    print(f"Fetching data for: {title}")
#    journal_info = get_journal_info(title)
#    journal_info['出版物标题'] = title
    
    # Append the data to the CSV file
#    with open(output_file_path, 'a', encoding='utf-8-sig', newline='') as f:
#        f.write(f"{journal_info['出版物标题']},{journal_info['实时影响因子']},{journal_info['平均审稿速度']},{journal_info['平均录用比例']}\n")
    
    # Pause to avoid overloading the server
#    time.sleep(1)

#print("Data successfully saved to 结果.csv")
#import time
#import pandas as pd
#import requests
#from bs4 import BeautifulSoup

# 读取 Excel 文件
#input_file = r'C:\Users\Administrator\Desktop\refine.xlsx'
#output_file = r'C:\Users\Administrator\Desktop\结果.csv'

# 从 Excel 文件中读取数据
#df = pd.read_excel(input_file)

# 假设期刊名在 'Title' 列中（请根据实际列名调整）
#titles = df['出版物标题'].tolist()

# 创建一个空列表来保存包含分区4的期刊名称
#filtered_titles = []

# 设置请求头以模拟浏览器行为
#headers = {
#    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
#}

# 遍历每个标题并查询网站
#for title in titles:
#    search_url = f"https://advanced.fenqubiao.com/search?q={title}"
    
    # 访问网站
#    response = requests.get(search_url, headers=headers)
#    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 查找分区信息（假设信息在某个特定的HTML元素中，需要根据实际情况调整）
#    division_info = soup.find('div', class_='division-class')  # 这是一个假设的例子
    
    # 如果分区包括4，则保存该期刊名称
#    if division_info and '4' in division_info.text:
#        filtered_titles.append(title)
    
    # 每次访问后等待5秒
#    time.sleep(2)

# 将结果保存到 CSV 文件中
#result_df = pd.DataFrame(filtered_titles, columns=['Title'])
#result_df.to_csv(output_file, index=False)

#print("处理完成，结果已保存到指定文件。")
#def getRuntime(a):
#    map={}
#    for i in a:
#        count=0
#        while not i[count]=='':
#            count=count+1
#        fun=i[0:count]
#        if i[count+2]=='n':
#            count=count+7
#            v=int(i[count:len(i)])
#            if fun in map.keys():
#                map[fun]=v-map[fun]
#            else:
#                map[fun]=v
#        else:
#            count=count+6
#            v=int(i[count:len(i)])
#            map[fun]=v-map[fun]
#    res=[]
#    for i in map:
#        res.append(i)
#    for i in range(0,len(res)):
#            res[i]=res[i]+'|'+str(map[res[i]])
#    return res
#def isInterval(intervalList,number):
#    high=len(intervalList)-1
#    low=0
#    while high>=low:
#        if 0<(number-intervalList[(high+low)//2][0])<=1000:
#            return 'True'   
#        elif 1000 <number - intervalList[(high+low)//2][0]:
#            low=(high+low)//2+1
#        elif 0>number -intervalList[(high+low)//2][0]:
#            high=(high+low)//2-1
#    return 'False'
#def hanshu (arr):
#    arr=sorted(arr)
#    even=0
#    odd=0
#    for i in range(0,len(arr)):
#        odd+=abs(arr[i]-(2*i+1))
#        even+=abs(arr[i]-(2*i+2))
#    if odd>even:
#        return odd
#    return even           
#def hanshu (arr):
#    b=sorted(arr)
#    even=0
#    odd=0
#    for i in range(0,len(b)):
#        even+=abs(b[i]-(2*i+2))
#        odd+=abs(b[i]-(2*i+1))
#    if odd>even:
#        return even,'even'
#    return odd,'odd'

#arr=[1,2,32,4,6,5,46,5,56,5,87,45,32]
#print(hanshu(arr))
#def hanshu (a):
#    length,b=len(a),[]
#    f=[0 for i in range(length+1)]
#    f[length]=1
#    for i in range (length-1,0,-1):
#        f[i]=f[i+1]*a[i]
#    tmp=1
#    for i in range(length):
#        b.append(tmp*f[i+1])
#        tmp*=a[i]
#    return b
#def hanshu (nestlist):
#    stack=[nestlist]
#    flatten_list=[]
#    while stack:
#        top=stack.pop()
#        if isinstance(top,list):
#            for elem in reversed(top):
#                stack.append(elem)#
#        else:
#            flatten_list.append(top)
#    return flatten_list
    #stack=[nestlist]
    #jieguo=[]
    #while stack:
    #    tem=stack.pop()
   #     if isinstance(tem,list):
   #         stack.append(tem )
#def hanshu (nestlist):
#    stack=[nestlist]
#    result=[]
#    while stack:
#        top=stack.pop()
#        if isinstance(top,list):
#            for item in reversed(top):
#                stack.append(item)
#        else:
#            result.append(top)
#    return result
#def hanshu(nestlist):
#    stack = [nestlist]
#    result = []
#    while stack:
#        top = stack.pop()
#        if isinstance(top, list):
#            for item in reversed(top):
#                stack.append(item)
#        else:#
#            result.append(top)
#    return result

#print(hanshu(nestlist=[1,1,[3,2,4,4],6,6]))            
#from PyPDF2 import PdfMerger
#from PIL import Image

# 文件路径
#pdf_path = "C:\\Users\\Administrator\\Desktop\\《现代物理》收录通知.pdf"
#png_path = "C:\\Users\\Administrator\\Desktop\\微信图片_20240913091214.png"
#output_pdf_path = "C:\\Users\\Administrator\\Desktop\\output_file.pdf"

# Step 1: 将PNG图片转换为PDF
#image = Image.open(png_path)
#image_pdf_path = "C:\\Users\\Administrator\\Desktop\\temp_image.pdf"
#image.save(image_pdf_path, "PDF")

# Step 2: 使用PdfMerger将PDF文件和转换后的PDF图片合并
#merger = PdfMerger()

# 添加PDF文件
#merger.append(pdf_path)

# 添加转换后的PDF图片
#merger.append(image_pdf_path)

# 保存合并后的PDF文件
#merger.write(output_pdf_path)
#merger.close()

#print("PDF已成功合并并输出到:", output_pdf_path)
#from PyPDF2 import PdfMerger
#from PIL import Image

# 文件路径
#pdf_path = "C:\\Users\\Administrator\\Desktop\\《现代物理》收录通知.pdf"
#png_path = "C:\\Users\\Administrator\\Desktop\\微信图片_20240913091214.png"
#output_pdf_path = "C:\\Users\\Administrator\\Desktop\\output_file.pdf"

# Step 1: 将PNG图片转换为PDF，确保图片模式为RGB
#image = Image.open(png_path)

# 如果图片是RGBA模式，转换为RGB模式
#if image.mode == 'RGBA':
#    image = image.convert('RGB')

#image_pdf_path = "C:\\Users\\Administrator\\Desktop\\temp_image.pdf"
#image.save(image_pdf_path, "PDF")

# Step 2: 使用PdfMerger将PDF文件和转换后的PDF图片合并
#merger = PdfMerger()

# 添加PDF文件
#merger.append(pdf_path)

# 添加转换后的PDF图片
#merger.append(image_pdf_path)

# 保存合并后的PDF文件
#merger.write(output_pdf_path)
#merger.close()

#print("PDF已成功合并并输出到:", output_pdf_path)
#def hanshu (s,t):
#    pos=0
#    for x in t:
#        while pos<len(s) and s[pos]!=x:
#            pos+=1
#        if pos==len(s):
#            return False
#        pos+=1
#    return True
#print(hanshu(s='abc',t='asdfasdf'))
#def hanshu (a,b):
#    if len (a) ==0:
#        return False
#    if len (b) ==0:
#        return True
#    s=[0 for _ in range (26)]
#    for i in a:
#        s[ord(i)-65]+=1
#    for i in b:
#        if s[ord(i)-65]==0:
#            return False
#        else:
#            s[ord(i)-65]-=1
#    return True
#print(hanshu(a='AABBCCDD',b='ABCE'))
#def hanshu (nums,target):
#    start=0
#    end=len(nums)-1
#    mid=start+(end-start)//2
#    while start+1<end:
#        if nums[mid]==target:
#            end=mid
#        elif nums[mid]<target:
#            start=mid
#        else:
#            end=mid
#    if nums[start]==target:
#        return start
#    if nums[end]==target:
#        return end
#    return -1

#print(hanshu(nums=[1,2,3,4,5,6,7],target=2))
#def hanshu (nums,target):
#    start=0
#    end=len(nums)-1
#    while start+1<end:
#        mid=start+(end-start)//2
#        if nums[mid]==target:
#            end=mid
#        elif nums[mid]<target:
#            start=mid
#        elif nums[mid]>target:
#            end=mid
#    if target-nums[start]<nums[end]-target:
#        return start
#    elif target-nums[start]>=nums[end]-target:
#        return end 
    
#print(hanshu(nums=[1,2,3,4,5,6],target=5))
#print(666)        
#import math
#print(math.sqrt(6))
#import math
#def hanshu (num):   
#    w=math.floor(math.sqrt(num))
#    while num%w!=0:
#        w-=1
#    return [w,num//w]
#print(hanshu(4787))
#import numpy as np
#normal_array = np.random.randn(3, 3)
#print("正态分布随机数：\n", normal_array)
#import numpy as np
#np.abs? 
#matrix = np.array([[1,2,3],[4,8,6]])
#rows = len(matrix)
#print("矩阵的行数:", rows)
#import cv2
#from matplotlib import pyplot as plt
#img=cv2.imread(r'C:\Users\Administrator\Desktop\微信图片_20240913091214.png')
#plt.imshow
#print('数据类型：{}，形状：{}'.format(type(img), img.shape))
#import cv2
#from matplotlib import pyplot as plt
#import os

# 图像路径
#image_path = 'C:\\Users\\Administrator\\Desktop\\图片1.jpg'

# 检查文件是否存在
#if not os.path.isfile(image_path):
#    print(f"文件不存在: {image_path}")
#else:
    # 读取图像
#    img = cv2.imread(image_path)

    # 检查图像是否读取成功
#    if img is None:
#        print("图像无法读取，请检查路径和文件")
#    else:
        # 打印数据类型和形状
#        print('数据类型：{}，形状：{}'.format(type(img), img.shape))

        # 转换 BGR 图像到 RGB 图像
#        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # 显示图像
#        plt.imshow(img_rgb)
#        plt.title('Image')
#        plt.axis('off')  # 关闭坐标轴
#        plt.show()
#import cv2
#from matplotlib import pyplot as plt
#img=cv2.imread('C:/Users/Administrator/Desktop/图片1.jpg')
#plt.imshow
#print("数据类型：{}，形状：{}".format(type(img),img.shape))
#import cv2
#from matplotlib import pyplot as plt

# 图片路径，使用原始字符串以避免转义字符问题
#image_path = r'C:\Users\Administrator\Desktop\20240913091214.png'

# 使用 OpenCV 读取图像
#img = cv2.imread(image_path)

# 检查图像是否成功读取
#if img is None:
#    print("无法读取图片，请检查路径是否正确")
#else:
    # OpenCV 以 BGR 格式读取图像，将其转换为 RGB 格式以便正确显示
#    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 创建一个 Matplotlib 图形
 #   plt.figure("图片预览")

    # 显示图像
#    plt.imshow(img_rgb)
#    plt.title('预览图')
#    plt.axis('off')  # 关闭坐标轴显示

    # 显示图形
#    plt.show()
#import cv2
#import matplotlib.pyplot as plt
#img=cv2.imread(r'C:\Users\Administrator\Desktop\6.jpg')
#plt.imshow(img)
#print('数据类型：{}，形状：{}'.format(type(img),img.shape)) 
#print(img.ndim)
#print(img.shape)
#print(img.dtype)
#import numpy as np
#st=[3.14,2.17,0,1,2]
#nd1=np.array(st)
#print(nd1)
#print(type(nd1))
#print(nd1.dtpye)
#d1=np.array([[[1,2,3],[7,5,6]],[[7,8,9],[10,11,12]]])
#print(d1.shape)
#d2=[[[1,2,3],[7,99,8]],[[4,5,6],[7,8,9]]]
#nd1=np.array(d2)
#print(nd1)
#print(nd1.shape)
#import numpy as np 
#print(np.random.random((4,4,3)))
#print(np.random.randint(low=1,high=50,size=(3,3)))
#print(np.zeros((2,5)))
#print(np.ones((3,4)))
#print(np.empty((3,4)))
#d=np.array([[1,2,3],[4,5,6]])
#print(d) 
#print(np.zeros_like(d))
#print(np.ones_like(d))
#print(np.empty_like(d))
#print(np.eye(14563)) 
#print(np.full((6,7),789))
#print(np.arange(1,10,1))
#print(np.linspace(1,10,1))
#np.random.seed(2019)
#ndl1=np.random.random(10)
#print(ndl1[3])
#print(ndl1[3:6])
#print(ndl1[1:6:2])
#print(ndl1[::-2])
#nd12=np.arange(25).reshape([5,5])
#nd12[1:3,1:3]
#print(nd12) 
#import numpy as np
#from numpy import random as nr
#a=np.arange(1,25,dtype=float)
#c1=nr.choice(a,size=(3,4))
#c2=nr.choice(a,size=(3,4),replace=False)
#c3=nr.choice(a,size=(3,4),p=a/np.sum(a))
#print(c1)#,c2,c3)
#print(a)
#print(c1)
#print(c2)
#print(c3)
#p=a/np.sum(a)
#print(p)
#q=a/sum(a)
#print(q)
#import numpy as np
#import matplotlib.pyplot as plt
#def sigmoid(x):
#    return 1/(1+np.exp(-x))
#x=np.linspace(-10,10,100)
#y=sigmoid(x)
#plt.plot(x,y)
#plt.title('Sigmoid Function')
#plt.xlabel('x')
#plt.ylabel('sigmoid(x)')
#plt.grid(True)
#plt.show()
#import numpy as np
#data=np.arange(10)
#print(data.reshape(2,5))
#print(data.reshape(5,-1))
#print(data.reshape(-1,5))
#print(data.reshape(-1,10))
#print(data.reshape(10,-1))
#import numpy as np
#data=np.arange(10)

#print(data)
#data.resize(2,5)
#print(data)
#import numpy as np

#arr = np.array([[1, 2, 3], [4, 5, 6]])
#flattened_arr = arr.ravel()  # 展平数组

#print("展平后的数组:", flattened_arr)  # 输出: [1 2 3 4 5 6]
#print("原数组:", arr)  # 输出: [[1 2 3] [4 5 6]]
#import numpy as np
#arr=np.arange(3).reshape(3,-1)
#print(arr)
#print(arr.shape)
#print(arr.squeeze().shape)
#print(arr.squeeze())
#arr1=np.arange(6).reshape(3,1,2,1) 
#print(arr1)    
#arr2=np.arange(24).reshape(2,3,4)
#print(arr2.shape)
#print(arr2.transpose(1,2,0).shape)
#print(arr2.transpose(1,2,0))
#import numpy as np
#a=np.array([1,2,3])
#b=np.array([4,5,6])
#c=np.append(a,b)
#print(c)
#import numpy as np
#a=np.arange(4).reshape(2,2)
#b=np.arange(4).reshape(2,2)
#print(a)
#print(b)
#c=np.append(a,b,axis=1)
#print(c.shape)
#print(c)
#import numpy as np
#data_train=np.random.randn(10000,2,3)
#print(data_train.shape)
#print(data_train)
#np.random.shuffle(data_train)
#print(data_train)
#batch_size=100
#for i in range(0,len(data_train),batch_size):
#    x_batch_sum=np.sum(data_train[i:i+batch_size])
#    print('第{}批次，该批次的数据之和为：{}'.format(i,x_batch_sum))
#import torch
#if __name__=='__main__':
#    print('Support CUDA ?:', torch.cuda.is_available())
#    x=torch.tensor([10.0])
#    y=x.cuda()
#    print(x)
    
#    y=torch.randn(2,3)
#    y=y.cuda()
#    print(y)
    
#    z=x+y
#    print(z)
#    from torch.backends import cudnn
#    print('Support cudnn ?:',cudnn.is_acceptable(x))
#import torch
#if __name__ == '__main__':
#    print('Support CUDA ?: ', torch.cuda.is_available())
    
#    x = torch.tensor([10.0]).cuda()  # 将 x 移动到 GPU
#    print(x)
    
#    y = torch.randn(2, 3).cuda()  # y 已经在 GPU 上
#    print(y)
    
#    z = x + y  # 现在 x 和 y 都在 GPU 上
#    print(z)
    
#    from torch.backends import cudnn
#    print('Support cudnn ?: ', cudnn.is_acceptable(x))
#import torch
#if __name__ == '__main__':
#    print('Support CUDA ?: ', torch.cuda.is_available())  # 检查是否有 GPU 支持，但不使用它
    
#    x = torch.tensor([10.0])  # 默认在 CPU 上创建张量
#    print(x)
    
#    y = torch.randn(2, 3)  # 在 CPU 上创建随机张量
#    print(y)
    
#    z = x + y  # 在 CPU 上进行运算
#    print(z)
    
#    from torch.backends import cudnn
#    print('Support cudnn ?: ', cudnn.is_acceptable(x))  # 仍然可以检查 cudnn 支持，但不使用 GPU
#import torch
#x=torch.tensor([1,2,3])
#y=torch.tensor([4,5,6])
#print(x)
#print(y)i
#z=x.add(y)
#print(z)
#x.add_(y)
#print(x)
#import torch
#torch.Tensor([1,2,3,4,5,6])
#d=torch.Tensor(2,3)
#print(d)
#t=torch.Tensor([[1,2,3],[4,5,6]])
#print(t)
#print(d)
#z=t.size()
#print(z)
#l=t.shape
#print(l)
#import torch
#t1=torch.tensor(1)
#t2=torch.Tensor(1)
#print('t1的值为{}，t1的数据类型为{}'.format(t1,t1.type()))
#print('t2的值为{}，t2的数据类型为{}'.format(t2,t2.type()))
#import torch
#print(torch.eye(2,2))
#print(torch.zeros(2,3))
#print(torch.linspace(1,10,4))
#print(torch.rand(2,3))
#print(torch.randn(2,3))
#print(torch.zeros_like(torch.rand(2,3)))
#import torch
#x=torch.randn(2,3)
#print(x.shape)
#print(x.shape)
#print(x.dim()) 
#print(x.view(3,2))
#y=x.view(-1)
#print(y.view(-1))
#print(y.size())
#print(x.shape)   
#z=torch.unsqueeze(y,1)
#print(z.size())
#print(z.numel())
'''import numpy as np
class Perceptron:
    def __init__(self,eta=0.01,n_iter=50,random_state=1):
        self.eta=eta
        self.n_iter=n_iter
        self.random_state=random_state
        
    def fit(self,X,y):
        rgen=np.random.RandomState(self.random_state)
        self.w_=rgen.normal(loc=0.0,scale=0.01,size=X.shape[1])
        self.b_=np.float_(0.)
        self.errors=[]
        
        for _ in range(self.n_iter):
            errors=0
            for xi,target in zip(X,y):
                update=self.eta*(target-self.predict(xi))
                self.w_+=update*xi
                self.b_+=update
                errors+=int(update !=0.0)
            self.errors.append(errors)
        return self
    
    def net_input(self,X):
        return np.dot(X,self.w_)+self.b_
    def predict(self,X):
        return np.where(self.net_input(X)>=0.0,1,0)
import pandas as pd
import os 
s='https://archive.ics.uci.edu/ml'\
    'machine-learning-databases/iris/iris.data'
print('From URL:',s)
s = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'


df=pd.read_csv(s,
                header=None,
                encoding='utf-8')
df.tail()

import matplotlib.pyplot as plt
import numpy as np
y=df.iloc[0:100,4].values
y=np.where(y=='Iris-setosa',0,1)
X=df.iloc[0:100,[0,2]].values
plt.scatter(X[:50,0],X[:50,1],
            color='red',marker='o',label='Setosa')
plt.scatter(X[50:100,0],X[50:100,1],
            color='blue',marker='s',label='Versicolor')
plt.xlabel('Sepal length [cm]')
plt.ylabel('Petal length [cm]')
plt.legend(loc='upper left')
plt.show()
ppn=Perceptron(eta=0.1,n_iter=10)
ppn.fit(X,y)
plt.plot(range(1,len(ppn.errors)+1),ppn.errors,marker='o')
plt.xlabel('Epochs')
plt.ylabel('Number of updates')
plt.show()
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np

def plot_decision_regions(X, y, classifier, resolution=0.02):
    markers = ('o', 's', '^', 'v', '<')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    
    lab = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    lab = lab.reshape(xx1.shape)
    plt.contourf(xx1, xx2, lab, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl, 0],
                    y=X[y==cl, 1],
                    alpha=0.8,
                    c=colors[idx],
                    label=f'Class {cl}',
                    edgecolor='black')
        
plot_decision_regions(X, y, classifier=ppn)
plt.xlabel('Sepal length [cm]')
plt.ylabel('Petal length [cm]')
plt.legend(loc='upper left')
plt.show()'''
'''import numpy as np
class AdalineGD:
    def __init__(self,eta=0.01,n_iter=50,random_state=1):
        self.eta=eta
        self.n_iter=n_iter
        self.random_state=random_state
    def activation (self,X):
        return X
    def net_input(self,X):
        return np.dot(X,self.w)+self.b
    def predict(self,X):
        return np.where(self.activation(self.net_input(X))>=0.5,1,0)
    def fit(self,X,y):
        regn=np.random.RandomState(self.random_state)
        self.w=regn.normal(loc=0.0,scale=0.01,size=X.shape[1])
        self.b=np.float(0.)
        self.losses=[]
        for i in range(self.n_iter):
            net_input=self.net_input(X)
            output=self.activation(net_input)
            errors=(y-output)
        return self'''
#import pandas as pd
#path=r'C:\Users\Administrator\Desktop\kagggle\machine learning\melb_data.csv'
#data=pd.read_csv(path)
#data.describe()
"""
import pandas as pd
path=r'C:\\Users\\Administrator\\Desktop\\kagggle\machine learning\melb_data.csv'
melbourne_data=pd.read_csv(path)
melbourne_data=melbourne_data.dropna(axis=0)
print(melbourne_data.columns)
y=melbourne_data.Price
melbourne_features=['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
x=melbourne_data[melbourne_features]
print(x.describe())
print(x.head())
"""
from sklearn.tree import DecisionTreeRegressor
print(666)
        

    
   
    