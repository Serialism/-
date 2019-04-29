#这是主函数,输出所有评论的分词结果
import os
import sys
import jieba
import codecs
import chardet
import numpy as np
import csv
import word_seperate


#停用词的录入
jieba.load_userdict('停用词表/stopwords.txt')
jieba.load_userdict('停用词表/中文停用词表.txt')
#中文额外词库的录入
jieba.load_userdict('中文分词词库整理/dict.txt')
jieba.load_userdict('中文分词词库整理/30万 中文分词词库.txt')
jieba.load_userdict('中文分词词库整理/dict2.txt')
#电影名和演员名的词典录入
jieba.load_userdict('电影名，演员名扩充词库/movie_dict.txt')#电影名
jieba.load_userdict('电影名，演员名扩充词库/director_dict.txt')#演员和导演名


for file in os.listdir('电影短评清洗'):
    word_seperate.txt_generator(file)

