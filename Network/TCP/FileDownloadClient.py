import socket

def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    dest_ip = input("服务器IP：")
    dest_port = int(input("服务器Port："))

    tcp_socket.connect((dest_ip, dest_port))

    file_name = input("要下载的文件名：")

    tcp_socket.send(file_name.encode("utf-8"))

    recv_data = tcp_socket.recv(1024)  # 1k大小

    if recv_data:
        with open("[附件]"+ file_name, "wb") as f:  # 
            f.write(recv_data)


if __name__ == "__main__":
    main()
