import time
from threading import Thread


def func(name):
    print(f"{name}开始")
    time.sleep(0.5)
    print(f"{name}结束")


if __name__ == '__main__':
    t1 = Thread(target=func, args=("线程1",))
    t2 = Thread(target=func, args=("线程2",))
    t1.start()
    t2.start()
    print("主线程结束")
