import socket
import re
import multiprocessing

def service_client(new_socket):

    request = new_socket.recv(1024).decode("utf-8")
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
        response = "HTTP/1.1 404 NOT FOUND\r\n\r\n"
        html_content = ("<h1>file not found :" + file_name + "<h1>").encode("utf-8")
    else:
        html_content = f.read()  # 注意 html_content 是 bytes 类型
        f.close()
        response = "HTTP/1.1 200 OK\r\n\r\n"

    new_socket.send(response.encode("utf-8"))
    new_socket.send(html_content)
    new_socket.close()


def main():

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.bind(("", 7890))

    tcp_server_socket.listen(128)

    while True:

        new_socket, addr_data = tcp_server_socket.accept()

        p = multiprocessing.Process(target=service_client, args=(new_socket,))  # 复制父进程资源
        p.start()

        new_socket.close()  # 比较重要！！！ Linux中一切皆文件，主进程和子进程均指向这个文件，如果主进程不关闭，子进程无法关闭
        # service_client(new_socket)

    tcp_server_socket.close()

if __name__ == "__main__":
    main()