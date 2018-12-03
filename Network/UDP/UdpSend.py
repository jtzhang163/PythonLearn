import socket

def main():
    # 创建了一个UDP套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(("",8888))  #可以在发送前绑定固定端口

    while True:

        # 从键盘获取数据
        send_data = input("请输入要发送的数据：")

        # 退出
        if send_data == "exit":
            break

        # 使用套接字收发数据
        udp_socket.sendto((send_data + "\r\n").encode("gbk"),("192.168.146.1",8080))

    # 关闭套接字    
    udp_socket.close()

if __name__ == "__main__":
    main()