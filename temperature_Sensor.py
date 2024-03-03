import socket
import time
import random

def temperature_sensor():
    # Bağlantı bilgileri
    server_address = ('localhost', 54321)

    while True:
        # TCP soketi oluştur
        tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Gateway ile bağlantı kur
            tcp_socket.connect(server_address)
            print("Temperature Sensor: Connected to Gateway")

            # Rastgele sıcaklık üret
            temperature = random.uniform(20, 30)

            # Zaman damgası ekle
            timestamp = time.time()

            # Mesajı oluştur ve gönder
            message = f"TEMP,{temperature},{timestamp}"
            tcp_socket.sendall(message.encode())

            print(f"Temperature Sensor: Sent - {message}")

            # Bekleme süresi (1 saniye)
            time.sleep(1)

        except Exception as e:
            print(f"Temperature Sensor Error: {e}")

        finally:
            # Soketi kapat
            tcp_socket.close()

if __name__ == "__main__":
    temperature_sensor()
