import os
import random
import time

from werkzeug.datastructures import FileStorage
from project.forms import *
from project import app, db, Config
from flask import render_template, flash, jsonify, session, url_for, request
from werkzeug.security import check_password_hash, generate_password_hash
from project.models import *
import settings as Config
from project import intergration


# 登录页面
@app.route('/', methods=['GET', 'POST'])
@app.route('/base', methods=['GET', 'POST'])
def base():
    # 默认一个uid
    session['uid'] = 1
    return render_template('base.html')

# @app.route('/login',methods=['POST','GET'])
# def login():
#     return render_template('login.html')
#
#
# @app.route('/LoginCheck', methods=['POST','GET'])
# def LoginCheck():
#     username = request.form.get('username')
#     password = request.form.get('password')
#     user = User.query.filter(User.username == username).first()
#     if user is not None:
#         if check_password_hash(user.password, password):
#             # 当user登录成功后直接记录user的uid，方便后续的使用
#             session['user'] = user.uid
#             return '1'
#     return '0'
#
# @app.route('/RegisterCheck',methods=['POST','GET'])
# def RegisterCheck():
#     username = request.form.get('username')
#     password = request.form.get("password")
#     user = User.query.filter(User.username == username).first()
#     if user is None:
#         newUser = User(username = username, password = generate_password_hash(password))
#         db.session.add(newUser)
#         db.session.commit()
#         return '1'
#     return '0'
#
#

# @app.route('/video',methods=['POST','GET'])
# def video():
#     if request.method == "POST":
#         path = Config.VIDEO_UPLOAD_DIR
#         JudgePath(path)
#         file = request.FILES.get("file")
#         filename = file.name
#         language = request.POST.get("language",'None')
#         mode = request.POST.get("mode","None")
#         if language is None:
#             print("fail to upload video")
#             return render(request, 'upload.html')
#         # 没有file的保存方法，只能create一个file然后写入
#         # 解决命名冲突
#         check = Video.objects.filter(name=filename).first()
#         while check is not None:
#             num = random.randint(1, 10)
#             filename = filename.split(".")[0] + str(num) + ".mp4"
#             check = Video.objects.filter(name=filename).first()
#         mp4 = open(os.path.join(path, filename), 'wb')
#         for chunk in file.chunks():
#             mp4.write(chunk)
#         mp4.close()
#         filename, text = VideoProcess(language, mode, filename, request.session.get('uid'))
#         filename = os.path.join(Config.video_display_dir, filename)
#         dic = {}
#         dic['filename'] = filename
#         dic['text'] = text
#     return render_template('upload.html')


@app.route('/video',methods=['POST', 'GET'])
def video():
    if request.method == "POST":
        video_folder_path = Config.video_folder_path
        image_folder_path = Config.image_folder_path
        file = request.files['file']
        filename = file.filename
        # print(filename)
        # 判断是否存在相同名称的视频
        check = os.path.join(video_folder_path, filename)
        while os.path.exists(check):
            num = random.randint(0, 9)
            filename = filename.split('.')[0] + str(num) + "." + filename.split('.')[1]
            check = os.path.join(video_folder_path, filename)
        # 存储视频文件
        file.save(os.path.join(video_folder_path, filename))
        # 提取视频中的帧并存储
        intergration.extra(video_folder_path, filename, image_folder_path, frequency = 5)

    return render_template('upload.html')


def JudgePath(path):
    if not os.path.exists(path):
        os.mkdir(path)
