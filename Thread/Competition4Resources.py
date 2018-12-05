import threading
import time


g_num = 0


def test1(num):
    global g_num

    mutex.acquire()

    for i in range(num):
        g_num += 1

    print("------in test1 g_num = %d----" % g_num)
    
    mutex.release()

def test2(num):
    global g_num

    mutex.acquire()

    for i in range(num):
        g_num += 1

    print("------in test2 g_num = %d----" % g_num)

    mutex.release()

mutex = threading.Lock()  # 创建一个互斥锁


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(500000,))

    t1.start()
    # time.sleep(1)

    t2.start()
    # time.sleep(1)

    time.sleep(5)

    print("------in main g_num = %d----" % g_num)


if __name__ == "__main__":
    main()