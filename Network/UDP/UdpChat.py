import socket

def send_msg(udp_socket):
    """发送数据"""
    dest_ip = input("请输入对方的ip：")
    dest_port = int(input("请输入对方的port："))
    send_data = input("请输入要发送的数据：")
    udp_socket.sendto( send_data.encode("gbk"), (dest_ip, dest_port))

def recv_msg(udp_socket):
    """接收数据"""

    recv_data = udp_socket.recvfrom(1024)
    print("发送方：%s \r\n接收到的数据: %s" % (str(recv_data[1]), recv_data[0].decode("gbk")))

def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(("",8888))

    while True:

        print("--------聊天器---------")
        print("1.发送消息")
        print("2.接收消息")
        print("0.退出系统")
        print("***********************")

        menu = input("请输入功能：")

        if menu == "0":
            break
        elif menu == "1":
            send_msg(udp_socket)
        elif menu == "2":
            recv_msg(udp_socket)
        else:
            print("输入有误！")

    udp_socket.close()

if __name__ == "__main__":
    main()
