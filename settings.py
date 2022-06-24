import os
# basedir是文件夹的根目录
basedir = os.path.abspath(os.path.dirname(__file__))
# 把根目录变成项目的根目录
basedir = os.path.join(basedir, 'project')

# video部分的参数
video_folder_path = os.path.join(basedir, 'static/videos')
image_folder_path = os.path.join(basedir, 'static/images')