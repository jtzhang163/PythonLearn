import socket

def main():
    # 创建了一个UDP套接字
    udp_socket = socket.socket( socket.AF_INET, socket.SOCK_DGRAM)

    # 从键盘获取数据
    send_data = input("请输入要发送的数据：")

    # 使用套接字收发数据
    udp_socket.sendto(send_data.encode("utf-8"),("192.168.146.1",8080))

    # 关闭套接字    
    udp_socket.close()

if __name__ == "_main_":
    main()