import os
import sys
import codecs
import chardet
#此函数用于转换字典的编码格式，jieba分词只支持UTF-8
#作为一个将来大概率会用到的编码转化工具放在这里
#运行程序中只需直接执行add_dict.py即可，不用理会这个

def convert(file, in_enc="GBK", out_enc="UTF-8"):
    """
    该程序用于将目录下的文件从指定格式转换到指定格式，默认的是GBK转到utf-8,jieba分词字典添加只允许UTF-8编码
    :param file:    文件路径
    :param in_enc:  输入文件格式
    :param out_enc: 输出文件格式
    :return:
    """
    in_enc = in_enc.upper()
    out_enc = out_enc.upper()
    try:
        print("convert [ " + file.split('\\')[-1] + " ].....From " + in_enc + " --> " + out_enc )
        f = codecs.open(file, 'r', in_enc)
        new_content = f.read()
        codecs.open(file, 'w', out_enc).write(new_content)
    # print (f.read())
    except IOError as err:
        print("I/O error: {0}".format(err))
#convert('中文分词词库整理/30万 中文分词词库.txt')
#convert('中文分词词库整理/42537条伪原创词库.txt',in_enc = 'GB18030')
#convert('电影名，演员名扩充词库/导演,演员信息.txt',in_enc = "GBK",out_enc = "UTF-8")
