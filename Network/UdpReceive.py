import socket

def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    udp_socket.bind(("",7788))  #必须绑定本地ip及port

    while True:

        recv_data = udp_socket.recvfrom(1024)

        recv_msg = recv_data[0]

        send_addr = recv_data[1]

        print("发送方：%s \r\n接收到的数据: %s" % (str(send_addr), recv_msg.decode("gbk")))

    udp_socket.close()

if __name__ == "__main__":
    main()
