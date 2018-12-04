import socket

def main():
    
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = input("服务器IP：")
    server_port = int(input("服务器端口："))
    server_addr = (server_ip, server_port)

    tcp_client_socket.connect(server_addr)

    send_data = input("要发送的数据：")
    tcp_client_socket.send(send_data.encode("gbk"))

    tcp_client_socket.close()

if __name__ == "__main__":
    main()
