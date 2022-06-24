import math
import os
from PIL import Image
from PIL import ImageFile
import cv2

# 实现对于视频自定义帧的提取


# 获取视频的时常
def get_video_duration(video_path):
    video = cv2.VideoCapture(video_path)
    if video.isOpened():
        # 得到视频中的帧速率
        rate = video.get(5)
        # 得到视频文件中的帧数
        frame_num = video.get(7)
        duration = frame_num/rate
        return int(duration)
    return -1


# 获取视频的第一帧作为这个视频的封面
# 和视频存储到同一个目录内
def get_first_frame(video_path):
    video = cv2.VideoCapture(video_path)
    # 逐帧读取视频
    while True:
        _, frame = video.read()
        if frame is None:
            return 0
        else:
            save_path = str(video_path).split(".")[0] + ".jpg"
            cv2.imwrite(save_path, frame)
        return 1


# 得到视频的帧率
def get_frame(video_path):
    # path: 文件的路径
    video = cv2.VideoCapture(video_path)
    # 得到每秒的帧率
    frame = video.get(cv2.CAP_PROP_FPS)
    # 返回整形变量
    return round(frame)


# 压缩图片文件
def compress_image(outfile, mb=50, quality=85, k=0.9):  # 通常你只需要修改mb大小
    """不改变图片尺寸压缩到指定大小
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param k: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """

    o_size = os.path.getsize(outfile) // 1024  # 函数返回为字节，除1024转为kb（1kb = 1024 bit）
    # print('before_size:{} after_size:{}'.format(o_size, mb))

    if o_size <= mb:
        return outfile

    ImageFile.LOAD_TRUNCATED_IMAGES = True  # 防止图像被截断而报错

    while o_size > mb:
        im = Image.open(outfile)
        x, y = im.size
        out = im.resize((int(x * k), int(y * k)), Image.ANTIALIAS)  # 最后一个参数设置可以提高图片转换后的质量
        try:
            out.save(outfile, quality=quality)  # quality为保存的质量，从1（最差）到95（最好），此时为85
        except Exception as e:
            print(e)
            break
        o_size = os.path.getsize(outfile) // 1024
    return outfile


def extract_frames(video_path, image_path, frequency):
    # 主操作
    video = cv2.VideoCapture()
    if not video.open(video_path):
        print("can not open the video")
        exit(1)
    # 检查文件夹是否存在
    if not os.path.exists(image_path):
        os.mkdir(image_path)
    # index 用来给图片编号
    index = 1
    # count用来记录当前的帧数
    count = 1
    # 得到视频的帧率
    frame = get_frame(video_path)
    # 设定每多少帧提取一次
    extract_frequency = round(frame / frequency)
    while True:
        _, frame = video.read()
        if frame is None:
            break
        if count % extract_frequency == 0:
            save_path = "{}/{:>03d}.jpg".format(image_path, index)
            cv2.imwrite(save_path, frame)
            index += 1
        count += 1
    video.release()
    # 打印出所提取帧的总数
    print("Totally save {:d} pics".format(index - 1))


def extra(video_folder_path, filename, image_folder_path, frequency):
    # video_folder_path: 视频文件夹的路径
    # filename: 视频文件的名称
    # image_folder: 图片文件夹路径
    # frequency: 1s需要截多少帧


    # 检查文件夹是否存在
    if not os.path.exists(video_folder_path):
        os.mkdir(video_folder_path)
    if not os.path.exists(image_folder_path):
        os.mkdir(image_folder_path)
    video_path = os.path.join(video_folder_path, filename)
    image_path = os.path.join(image_folder_path, filename.split(".")[0])
    # 判断视频的时长是否过长
    video_duration = get_video_duration(video_path)
    if video_duration >= 50:
        print('the video is too long')
        return 0
    # 得到视频的第一帧作为视频的封面
    get_first_frame(video_path)
    # 提取帧
    extract_frames(video_path, image_path, frequency)
    # 压缩图片
    for pic in os.listdir(image_path):
        compress_image(os.path.join(image_path, pic))


# video_folder_path = os.path.join(os.getcwd(), 'video')
# image_folder_path = os.path.join(os.getcwd(), 'image')
# frequency = 10
# filename = 'test1.mp4'
# extra(video_folder_path, filename, image_folder_path, frequency)

