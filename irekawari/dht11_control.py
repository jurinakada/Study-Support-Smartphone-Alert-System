import adafruit_dht
import board


class DHT11Control:

    def __init__(self):
        self.sensor = adafruit_dht.DHT11(board.D16)

    def read(self):
        try:
            temperature = self.sensor.temperature
            humidity = self.sensor.humidity

            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")

            return humidity, temperature

        except RuntimeError:
            #DHT11 sometimes fails. Just try again later.
            return None, None
