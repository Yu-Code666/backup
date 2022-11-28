# backup1为简单的复制小文件的版本

import os

file_path = r'D:\我\我的\研究生学习\研0\实习\备份\test.txt'

if os.path.isfile(file_path):
    # 生成新文件名
    dot_index = file_path.rfind('.')
    new_file_path = file_path[:dot_index] + '_copy1' + file_path[dot_index:]

    # 打开原文件，读取文件信息
    with open(file_path, 'rb') as old_file:
        old_file_content = old_file.read()
        # old_file_content = old_file_content.decode('utf-8')
        # print(old_file_content)

    # 创建新文件并写入数据
    # open一个不存在的文件时是会创建一个新文件吗:是的
    # 如果要open的这个文件已经存在了，read方法是覆盖重写，还是续写在后面呢：是覆盖重写
    with open(new_file_path,'wb') as new_file:
        new_file.write(old_file_content)
    # 我open了这个新文件，以二进制的形式将数据写入新文件，但是只有在新文件和旧文件编码格式相同的情况下才是正确的
    # 不是文本文件能这样复制吗