import socket

def main():

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.bind(("",9999))

    tcp_server_socket.listen(128)

    while True:
        print("等待一个新的客户端的到来...")
        tcp_client_socket, client_addr =  tcp_server_socket.accept()
        print("一个新的客户端已经到来：" + str(client_addr))
        while True:
            recv_data = tcp_client_socket.recv(1024)

            # recv解堵塞或者recv返回值为空 表示服务完成
            # 客户端执行close()后，返回recv_data为空
            if recv_data:
                print("客户端发送过来的数据是：" + recv_data.decode("gbk"))
                tcp_client_socket.send("收到：".encode("gbk") + recv_data)  

            else:
                break           

        tcp_client_socket.close()
        print("已经为这个客户端服务完毕！")

    tcp_server_socket.close()

if __name__ == "__main__":
    main()
