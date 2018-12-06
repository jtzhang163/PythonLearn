import time
import threading


def sing():
    """唱歌 5 秒钟"""
    for i in range(5):
        time.sleep(1)
        print("唱歌... %d " % i)


def dance():
    """跳舞 5 秒钟"""
    for i in range(5):
        time.sleep(1)
        print("跳舞... %d " % i)


def main():

    # 使用多线程
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()

    # 查看线程数
    while True:
        time.sleep(1)
        length = len(threading.enumerate())
        if length < 2:
            break
        print(length)


if __name__ == "__main__":
    main()