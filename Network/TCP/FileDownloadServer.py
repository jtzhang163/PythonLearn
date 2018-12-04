import socket

def main():

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.bind(("",9999))

    tcp_server_socket.listen(128)

    tcp_client_socket, client_addr =  tcp_server_socket.accept()
    print("一个新的客户端已经到来：" + str(client_addr))

    file_name = tcp_client_socket.recv(1024).decode("gbk")
    print("客户端需要下载的文件是：" + file_name)

    file_content = None

    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("打开文件 %s 失败： %s " % (file_name, ret))


    if file_content:
        tcp_client_socket.send(file_content)  
          

    tcp_client_socket.close()

    tcp_server_socket.close()

if __name__ == "__main__":
    main()
