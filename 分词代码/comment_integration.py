import csv
import os

#csv_to_tet()函数将csv的电影短评清洗并转化为txt文件，在'电影短评清洗'文件夹下
#file_directory是文件的上层目录，譬如'151-200'，'101-150'，file_name 是文件的名称
def csv_to_txt(file_directory,file_name):
    file_name_cut = file_name.strip('.csv')
    data = csv.reader(open('电影短评/'+file_directory+'/'+ file_name,"rt"))
    content = []
    for row in data:
        content.append(row[5])
    file = open('电影短评清洗/'+ file_name_cut + '.txt','w+')
    file.write(file_name_cut)
    for item in content:
        file.write(str(item)+"\n")
    file.close()


#一层层打开并遍历电影短评中的文件清洗出所有的电影评论与相关联的id到'电影短评清洗文件夹下'
comment_file_path = '电影短评'
file_path_list = []
for file in os.listdir(comment_file_path):
    file_path = os.path.join(file)
    file_path_list.append(file_path)

file_path_list.remove('.DS_Store')
print(file_path_list)
for item1 in file_path_list:
    comment_file = os.listdir('电影短评/'+item1)
    for item2 in comment_file:
        csv_to_txt(item1,item2)



