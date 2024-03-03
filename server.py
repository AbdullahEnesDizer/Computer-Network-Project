import socket
import threading


def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    # Gelen veriyi oku
    data = client_socket.recv(1024)
    print(f"Received data: {data.decode()}")

    # Bağlantıyı kapat
    client_socket.close()
    print(f"Connection with {client_address} closed")


# Bağlantı bilgileri
server_address = ('localhost', 54321)

# TCP soketi oluştur
tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Soketi belirtilen adrese ve port numarasına bağla
tcp_server.bind(server_address)

# Bağlantıları dinle
tcp_server.listen()

print(f"Server is listening on {server_address}")

while True:
    # Bağlantıyı kabul et
    client_socket, client_address = tcp_server.accept()

    # Her bağlantı için ayrı bir iş parçacığı oluştur
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
