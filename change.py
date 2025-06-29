#!/usr/bin/env -S uv run --script

import os
import random
import string

# 设置文件夹路径（当前目录）
DIR = os.getcwd()
SELF_FILENAME = os.path.basename(__file__)

# 随机生成一行文本
def random_line(length=40):
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length))

# 随机生成文件名
def random_filename(extension=".txt"):
    name = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{name}{extension}"

# 操作 1: 添加一个随机内容的文件
def add_file():
    filename = random_filename()
    path = os.path.join(DIR, filename)
    with open(path, 'w') as f:
        for _ in range(random.randint(3, 10)):
            f.write(random_line() + "\n")
    print(f"添加文件: {filename}")

# 操作 2: 给现有文件添加或删去一行
def modify_line_add_or_delete(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    if random.choice([True, False]) or not lines:  # 添加一行
        index = random.randint(0, len(lines))
        lines.insert(index, random_line() + "\n")
        print(f"添加一行到: {file_path}")
    else:  # 删除一行
        index = random.randint(0, len(lines) - 1)
        lines.pop(index)
        print(f"删除一行从: {file_path}")
    
    with open(file_path, 'w') as f:
        f.writelines(lines)

# 操作 3: 替换某个文件的随机一行
def replace_line(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    if lines:
        index = random.randint(0, len(lines) - 1)
        lines[index] = random_line() + "\n"
        with open(file_path, 'w') as f:
            f.writelines(lines)
        print(f"替换一行于: {file_path}")
    else:
        print(f"{file_path} 是空文件，跳过替换")

# 操作 4: 删除一个文件
def delete_file(file_path):
    os.remove(file_path)
    print(f"删除文件: {file_path}")

# 主函数
def main():
    # 当前目录下的非隐藏文本文件，排除自身脚本
    files = [
        f for f in os.listdir(DIR)
        if os.path.isfile(f) and not f.startswith('.') and f != SELF_FILENAME
    ]
    text_files = [f for f in files if f.endswith('.txt')]

    # 随机选择一个操作
    operation = random.choice(['add', 'mod_line', 'replace_line', 'delete'])
    
    if operation == 'add':
        add_file()
    elif operation == 'mod_line' and text_files:
        modify_line_add_or_delete(random.choice(text_files))
    elif operation == 'replace_line' and text_files:
        replace_line(random.choice(text_files))
    elif operation == 'delete' and text_files:
        delete_file(random.choice(text_files))
    else:
        print("没有可操作的文件，执行添加文件操作。")
        add_file()

if __name__ == "__main__":
    main()
