import socket
import re
import select

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

    # 创建一个epoll对象
    epl = select.epoll()
    # 将监听套接字对应的fd（文件描述符）注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)

    tcp_server_socket.listen(128)

    fd_event_dict = dict()

    while True:

        fd_events = epl.poll()  # 默认会堵塞，直到os检测到数据到来
        # [(fd, event),(fd, event),...]
        for fd, event in fd_events:
            if fd == tcp_server_socket.fileno():
                new_socket, addr_data = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                recv_data = fd_event_dict[fd].recv(1024)
                if recv_data:
                    request = recv_data.decode("utf-8")
                    service_client(fd_event_dict[fd], request)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    tcp_server_socket.close()

if __name__ == "__main__":
    main()
