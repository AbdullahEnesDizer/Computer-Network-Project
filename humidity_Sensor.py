import socket
import time
import random

def humidity_sensor():
    # Bağlantı bilgileri
    server_address = ('localhost', 54321)  # Aynı gateway'e bağlanmak için

    # UDP soketi oluştur
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            # Rastgele nem üret
            humidity = random.uniform(40, 90)

            # Zaman damgası ekle
            timestamp = time.time()

            # Sadece nem değeri 80'i aştığında gönder
            if humidity > 80:
                # Mesajı oluştur ve gönder
                message = f"HUMIDITY,{humidity},{timestamp}"
                udp_socket.sendto(message.encode(), server_address)
                print(f"Humidity Sensor: Sent - {message}")

            # 'ALIVE' mesajını her 3 saniyede bir gönder
            if int(timestamp) % 3 == 0:
                alive_message = "ALIVE"
                udp_socket.sendto(alive_message.encode(), server_address)
                print(f"Humidity Sensor: Sent - {alive_message}")

            # Bekleme süresi (1 saniye)
            time.sleep(1)

    except Exception as e:
        print(f"Humidity Sensor Error: {e}")

    finally:
        # Soketi kapat
        udp_socket.close()

if __name__ == "__main__":
    humidity_sensor()
