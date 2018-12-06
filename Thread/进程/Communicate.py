import multiprocessing

def download_from_web(q):
    data = [11, 22, 33, 44]
    for tmp in data:
        q.put(tmp)
    print("...下载器已经下载完毕...")

def analysis_data(q):
    waitting_data = list()  # 或者[]
    while True:
        if q.empty():
            break
        data = q.get();
        waitting_data.append(data)
    print(waitting_data)

def main():
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()

if __name__ == "__main__":
    main()
