import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'db.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # video部分的参数
    VIDEO_UPLOAD_DIR = os.path.join(basedir, 'static/resource')
    input_path = os.path.join(basedir, 'static/resource')
    output_path_Ch = os.path.join(basedir, 'static/temp/Chinese')
    output_path_En = os.path.join(basedir, 'static/temp/English')

    video_display_dir = "../static/resource"