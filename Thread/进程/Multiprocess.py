#import threading
import time
import multiprocessing

def test1():
    while True:
        time.sleep(1)
        print("-------1-------")

def test2():
    while True:
        time.sleep(1)
        print("-------2-------")


def main():

    #t1 = threading.Thread(target=test1)
    #t2 = threading.Thread(target=test2)
    #t1.start()
    #t2.start()

    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
