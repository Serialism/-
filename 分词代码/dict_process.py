#此文件用于处理字典的格式，用于导入jieba
#字典处理一遍就够，已经经过数据清洗且生成的新字典都存在于‘中文分词词库整理’这一目录下，程序已不必再次运行
#扩充词典的方法在‘dict_add.py’中
#我保留此文件做为未来有可能需要处理制作的新词典的操作参考（譬如电影名词典，演员词典）。
import xlrd
import xlwt

'''
x1 = open('中文分词词库整理/30万 中文分词词库.txt','r',encoding = 'GBK')
x2 = open('中文分词词库整理/42537条伪原创词库.txt','r',encoding = 'UTF-8')
x3 = open('中文分词词库整理/dict.txt','r',encoding = 'UTF-8')
x4 = open('中文分词词库整理/fingerDic.txt')
x5 = open('中文分词词库整理/百度分词词库.txt',encoding = 'GBK')
---------------------------------------------------------------------------------------------------------------
data1 = [line.strip().replace('\t','1').split('1') for line in x1.readlines()]
dict1 =[]
for i in range(len(data1)-1):
    dict1.append(data1[i][2])

-------------------------------------------------------------------------------------------------------
data2 = [line.replace('→','/n').strip().split('/n') for line in x2.readlines()]
dict_2 = []
for i in range(len(data2)-1):
    for j in range(2):
        dict_2.append(data2[i][j-1])
dict2 = [item.lstrip() for item in dict_2]
#把数组写回dict2.txt
print(dict2)
fp = open('中文分词词库整理/dict2.txt','w+')
for item in dict2:
            fp.write(str(item)+"\n")
fp.close()
-------------------------------------------------------------------------------------------------------------------
#dict3
data3 = [line.strip() for line in x3.readlines()]
dict3 = data3
--------------------------------------------------------------------------------------------------------------------
#dict4
data4 = [line.strip() for line in x4.readlines()]
dict4 = data4
-------------------------------------------------------------------------------------------------------------------
#dict5
#data5 = [line.strip().replace('\x00',',').split(',')  for line in x5.readlines()]
'''
'''
----------------------------------------------------------------------------------
f = open('电影名，演员名扩充词库/豆瓣电影列表.txt','r',encoding = 'UTF-16')
names = [line.split('\t') for line in f.readlines()]
print(names)
name_1 = []
for i in range(200):
    name_1.append(names[i][1])
movie_name = []
for line in name_1:
    line = line.replace('\n', '')
    line = line.replace("\'",'')
    movie_name.append(line)
print(movie_name)
file = open('电影名，演员名扩充词库/movie_dict.txt','w')
for item in movie_name:
    file.write(str(item)+"\n")
file.close()
'''
'''
#演员，导演的词库整理
-----------------------------------------------------------------------------------------------------
f = open('电影名，演员名扩充词库/导演,演员信息.txt')
names = [line.strip().split('\t') for line in f.readlines()]
print(names)
all_names = []
for item in names:
    for i in range(2):
        all_names.append(item[i])

print(all_names)
file = open('电影名，演员名扩充词库/director_dict.txt','w')
for item in all_names:
    file.write(str(item.strip())+"\n")
file.close()
'''