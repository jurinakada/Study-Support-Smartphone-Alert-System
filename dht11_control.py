# Temperature and Humidity
# This program uses DHT11 provided by university

import time
from DHT11 import DHT11


class DHT11Control:
    def __init__(self, pin=14, interval=5):
        self.sensor = DHT11(pin)
        self.interval = interval

    def read(self):
        humidity, temperature = self.sensor.read_data()

        # If the sensor fails to read data
        if humidity == 0.0 and temperature == 0.0:
            print("Failed to read DHT11 data")
            return None, None

        print(f"Temperature: {temperature}°C  Humidity: {humidity}%")
        return humidity, temperature

    def start_measuring(self):
        try:
            while True:
                self.read()
                time.sleep(self.interval)

        except KeyboardInterrupt:
            print("DHT11 measurement stopped")


# testing parts
if __name__ == "__main__":
    dht = DHT11Control(pin=14, interval=5)
    dht.start_measuring()