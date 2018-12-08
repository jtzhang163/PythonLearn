import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()

def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()
    with open(img_name,"wb") as f:
        f.write(img_content)

def main():
    gevent.joinall([
        gevent.spawn(downloader, "3.jpg", "https://rpic.douyucdn.cn/live-cover/appCovers/2018/12/04/4434455_20181204164507_small.jpg"),
        gevent.spawn(downloader, "4.jpg", "https://rpic.douyucdn.cn/live-cover/appCovers/2018/10/07/5469810_20181007004310_small.jpg")
    ])

if __name__ == "__main__":
    main()