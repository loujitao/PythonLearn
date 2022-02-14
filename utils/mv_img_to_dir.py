import os
import xlwt, time, shutil
import uuid

# 获取当前文件所在绝对目录路径
this_path = os.path.abspath('E:/BaiduNetdiskDownload/各类手机壁纸')
# 定义个列表存放每个文件路径，便于后期操作
file_list = []


# 创建个方法，统计每个文件路径，并追加列表中。用到了递归
def get_all_file(dir_path):
    for file in os.listdir(dir_path):
        # print(file)
        filepath = os.path.join(dir_path, file)
        # print(filepath)
        if os.path.isdir(filepath):
            get_all_file(filepath)
        else:
            file_list.append(filepath)
    return file_list


# 执行上面方法，把每个文件绝对路径追加到列表中
get_all_file(this_path)

# 定义总目录名，准备存放列表中所有文件
target_dir = 'D:/wq'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 创建一个excel表存放文件路径信息，第一列是目录，第二列是文件名
wb = xlwt.Workbook()
sh = wb.add_sheet('文件和目录信息')
row_count = 0
for file in file_list:
    dir_filename = os.path.split(file)
    sh.write(row_count, 0, dir_filename[0])
    sh.write(row_count, 1, dir_filename[1])
    row_count += 1

wb.save("文件路径信息统计结果.xls")

# 定义个日志存放异常信息以及重名文件
f_fail = open('失败记录.log', 'a')  # 追加模式
f_same = open('重名文件信息.log', 'a')  # 追加模式
# 移动文件

print("开始移动文件.................")
for file in file_list:
    if os.path.exists(file):
        file_name = str(uuid.uuid1())[0:6] +" "+os.path.split(file)[1]
        target_path = os.path.join(target_dir, file_name)
        if os.path.exists(target_path):
            print(target_dir + "目录中----" + file_name + "----已经存在,移动失败")
            f_same.write(target_dir + "目录中----" + file_name + "----已经存在,移动" + file + "失败\r\n")
        else:
            shutil.move(file, target_path)
        time.sleep(0.1)
    else:
        print(file, "not exist")
        f_fail.write(file + "----不存在\r\n")
        print(file + "----不存在\r\n")
        time.sleep(0.5)
print("程序执行完毕,3秒后退出")
time.sleep(3)