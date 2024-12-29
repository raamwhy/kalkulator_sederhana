import random
import time

class IoTDevice:
    def __init__(self, location):
        self.location = location
        self.temperature = 0

    def read_temperature(self):
        # Simulasi pembacaan sensor suhu
        self.temperature = random.uniform(20.0, 35.0)  # Suhu acak antara 20 dan 35 derajat Celsius
        return self.temperature

class IoTServer:
    def __init__(self):
        self.temperature_data = {}

    def receive_data(self, location, temperature):
        self.temperature_data[location] = temperature
        print(f"Data diterima dari {location}: {temperature:.2f}°C")

    def analyze_data(self):
        for location, temperature in self.temperature_data.items():
            if temperature > 30.0:
                print(f"Peringatan: Suhu di {location} terlalu tinggi! ({temperature:.2f}°C)")
            else:
                print(f"Suhu di {location} normal. ({temperature:.2f}°C)")

# Inisialisasi perangkat IoT di dua lokasi
device_warehouse = IoTDevice("Gudang A")
device_factory = IoTDevice("Pabrik B")

# Inisialisasi server IoT
server = IoTServer()

# Simulasi pengiriman data selama beberapa kali
for _ in range(5):
    # Perangkat membaca suhu
    temp_warehouse = device_warehouse.read_temperature()
    temp_factory = device_factory.read_temperature()

    # Data dikirim ke server
    server.receive_data(device_warehouse.location, temp_warehouse)
    server.receive_data(device_factory.location, temp_factory)

    # Analisis data di server
    server.analyze_data()

    # Delay untuk simulasi waktu nyata
    time.sleep(2)
