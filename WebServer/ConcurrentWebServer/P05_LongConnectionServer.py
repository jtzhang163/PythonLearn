import socket
import time

def main():

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 7890))
    tcp_server_socket.setblocking(False)  # 设置为非阻塞
    tcp_server_socket.listen(128)

    client_sockets = list()

    while True:

        time.sleep(1)

        try:
            new_client, client_addr = tcp_server_socket.accept()
        except Exception as ex:
            print("—————没有新的客户端连接—————")
        else:
            new_client.setblocking(False)
            client_sockets.append(new_client)

        for client_socket in client_sockets:
            try:
                recv_data = client_socket.recv(1024)
            except Exception as ex:
                print(ex)
                print("—————这个客户端没有发送过来数据—————")
            else:
                if recv_data:
                    print("—————客户端发送过来了数据>>>", recv_data.decode("utf-8"))
                else:   
                    client_sockets.remove(client_socket)
                    client_socket.close()
                    print("—————客户端已经关闭—————")


if __name__ == "__main__":
    main()