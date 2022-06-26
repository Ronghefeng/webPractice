import socket
import threading


def handle_msg(conn, address):

    while True:

        client_data = conn.recv(1024).decode()

        # 接收信息
        if client_data == "exit":  # 判断是否退出连接
            exit("通信结束")

        print("来自%s的客户端向你发来信息：%s" % (address, client_data))

        conn.sendall(f"服务器已经收到 {address} 的信息".encode())  # 回馈信息给客户端


if __name__ == "__main__":

    ip_port = ("127.0.0.1", 9999)

    sk = socket.socket()  # 创建套接字
    sk.bind(ip_port)  # 绑定服务地址
    sk.listen(5)  # 监听连接请求

    print("启动socket服务，等待客户端连接...")

    while True:  # 一个死循环，直到客户端发送‘exit’的信号，才关闭连接

        conn, address = sk.accept()  # 等待连接，此处自动阻塞

        threading.Thread(target=handle_msg, args=(conn, address)).start()
