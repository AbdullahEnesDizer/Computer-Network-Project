import socket
import time
import random

def gateway():
    # Bağlantı bilgileri
    server_address = ('localhost', 54321)

    # TCP soketi oluştur
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # UDP soketi oluştur
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Gateway ile bağlantı kur
        tcp_socket.connect(server_address)
        tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

        print("Gateway: Connected to Server")

        while True:
            # TEMPERATURE SENSOR
            try:
                # Rastgele sıcaklık üret
                temperature = random.uniform(20, 30)

                # Zaman damgası ekle
                timestamp = time.time()

                # Mesajı oluştur ve gönder
                message = f"TEMP,{temperature},{timestamp}"
                tcp_socket.sendall(message.encode())

                print(f"Gateway: Sent - {message}")

                # Bekleme süresi (1 saniye)
                time.sleep(1)

            except Exception as e:
                print(f"Temperature Sensor Error: {e}")
                # Hata durumunda 'TEMP SENSOR OFF' mesajını gönder
                error_message = "TEMP SENSOR OFF"
                tcp_socket.sendall(error_message.encode())
                print(f"Gateway: Sent - {error_message}")

            # HUMIDITY SENSOR
            try:
                # Rastgele nem üret
                humidity = random.uniform(40, 90)

                # Zaman damgası ekle
                timestamp = time.time()

                # Sadece nem değeri 80'i aştığında gönder
                if humidity > 80:
                    # Mesajı oluştur ve gönder
                    message = f"HUMIDITY,{humidity},{timestamp}"
                    udp_socket.sendto(message.encode(), server_address)
                    print(f"Gateway: Sent - {message}")

                # 'ALIVE' mesajını her 3 saniyede bir gönder
                if int(timestamp) % 3 == 0:
                    alive_message = "ALIVE"
                    udp_socket.sendto(alive_message.encode(), server_address)
                    print(f"Gateway: Sent - {alive_message}")

                # Bekleme süresi (1 saniye)
                time.sleep(1)

            except Exception as e:
                print(f"Humidity Sensor Error: {e}")
                # Hata durumunda 'HUMIDITY SENSOR OFF' mesajını gönder
                error_message = "HUMIDITY SENSOR OFF"
                tcp_socket.sendall(error_message.encode())
                print(f"Gateway: Sent - {error_message}")

    except Exception as e:
        print(f"Gateway Error: {e}")

    finally:
        # Soketleri kapat
        tcp_socket.close()
        udp_socket.close()

if __name__ == "__main__":
    gateway()
