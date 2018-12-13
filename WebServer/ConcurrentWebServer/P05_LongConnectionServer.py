import socket
import re

def service_client(new_socket, request):

    request_lines = request.splitlines()

    # GET /Index.html HTTP/1.1
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    try:
        f = open("./html" + file_name, "rb")
    except:
        response_header = "HTTP/1.1 404 NOT FOUND\r\n\r\n"
        response_body = ("<h1>file not found: " + file_name + "<h1>").encode("utf-8")
    else:
        response_body = f.read()  # 注意 response_body 是 bytes 类型
        f.close()
        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d" % len(response_body)
        response_header += "\r\n"

    new_socket.send(response_header.encode("utf-8"))
    new_socket.send(response_body)
    new_socket.close()


def main():

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(("", 7890))
    tcp_server_socket.setblocking(False)
    tcp_server_socket.listen(128)

    client_sockets = list()

    while True:
        try:
            new_socket, addr_data = tcp_server_socket.accept()
        except Exception as ex:
            pass
        else:
            client_sockets.append(new_socket)
            new_socket.setblocking(False)

        for client_socket in client_sockets:
            try:
                recv_data = client_socket.recv(1024)
            except Exception as ex2:
                pass
            else:
                if recv_data:
                    request = recv_data.decode("utf-8")
                    service_client(client_socket, request)
                else:
                    client_socket.close()
                    client_sockets.remove(client_socket)

    tcp_server_socket.close()

if __name__ == "__main__":
    main()
