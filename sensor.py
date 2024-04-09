from datetime import datetime

class Sensor:
    def __init__(self, sensor_type, location, data=None):
        self.sensor_type = sensor_type
        self.location = location
        self.data = data or []

    def add_data(self, data_point):
        self.data.append(data_point)

    def get_data(self):
        current_hour = datetime.now().hour
        if current_hour < len(self.data):
            return self.data[current_hour]
        else:
            return None

    def __str__(self):
        current_data = self.get_data()
        all_data = self.data
        return f"Sensor: Type: {self.sensor_type}, Location: {self.location}, Current Data: {current_data}, All Data: {all_data}"

    def print_current_data(self):
        current_data = self.get_data()
        print(f"Sensor: Type: {self.sensor_type}, Location: {self.location}, Current Hour Data: {current_data}")

    def print_all_data(self):
        print(f"Sensor: Type: {self.sensor_type}, Location: {self.location}, All Data: {self.data}")


sensor1 = Sensor(sensor_type="Air Quality", location="Indoor", data=[10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60])
sensor2 = Sensor(sensor_type="Temperature", location="Living Room", data=[15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65])
sensor3 = Sensor(sensor_type="Rainfall", location="Backyard", data=[20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70])

sensor1.print_current_data()
sensor1.print_all_data()

sensor2.print_current_data()
sensor2.print_all_data()

sensor3.print_current_data()
sensor3.print_all_data()

class SensorType:
    def __init__(self, name, units):
        self.name = name
        self.units = units

    def get_info(self):
        """
        Returns a string with information about the sensor type.

        :return: String with information about the sensor type
        """
        return f"Sensor Type: {self.name}, Units: {self.units}"

    def __str__(self):
        """
        Representation of the sensor type object as a string.
        """
        return self.get_info()
