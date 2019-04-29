import jieba

def stop_words_list(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='UTF-8').readlines()]
    return stopwords
#将两个停用词表分别整理成数组保存至stop_words1和stop_word2中
stop_words1 = stop_words_list('停用词表/stopwords.txt')
stop_words2 = stop_words_list('停用词表/中文停用词表.txt')
#该函数将'电影短评'中的评论文件分词并整理成数组返回
def word_seperate(file):
    f = open('电影短评清洗/'+file)
    words = [list(jieba.cut(item)) for item in f.readlines()]
    return words
#该函数将整理后的数组words进行分词处理，运用了两个分词包stop_words1和stop_words2
def stopwords_cut(words):
    for item in words:
        for word in item:
            if word in stop_words1 or word  in stop_words2 or word == '\t' or word == '\n' or word == '，' or word == '“' or word == '”' or word == '。' or word == '？':
                item.remove(word)
    return words
#该函数将file文件清洗分词后的结果保存至‘电影短评分词结果’
def txt_generator(file):
    final_file = open('电影短评分词结果/'+'word_'+file,'w')
    result = stopwords_cut(word_seperate(file))
    for item in result:
        for word in item:
            final_file.write(str(word).strip()+'\t')
        final_file.write('\n')
    final_file.close()




