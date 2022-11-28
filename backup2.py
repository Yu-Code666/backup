# backup1为简单的复制小文件的版本

import os

file_path = r'D:\我\我的\研究生学习\研0\实习\备份\test.txt'

if os.path.isfile(file_path):
    # 生成新文件名
    dot_index = file_path.rfind('.')
    new_file_path = file_path[:dot_index] + '_copy2' + file_path[dot_index:]

    # 打开原文件，读取文件信息
    with open(file_path, 'rb') as old_file:
        # 不断得读取每行数据，直到
        while True:
            # 一次读取一行的数据
            old_file_content_line = old_file.readline()

            if not old_file_content_line:
                break

            with open(new_file_path, 'wb') as new_file:
                new_file.write(old_file_content_line)



