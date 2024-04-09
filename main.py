from sensor import Sensor, SensorType
from DataCollector import DataCollector
from CentralSystem import CentralSystem


class IoTDevice:
    def __init__(self, device_id):
        self.device_id = device_id
        self.sensors = []
        self.data_collector = DataCollector()
        self.initialize_sensors()

    def initialize_sensors(self):
        # Generate data for sensors
        data_sensor1 = [10]  # Example data for the first sensor
        data_sensor2 = [15]  # Example data for the second sensor
        data_sensor3 = [20]  # Example data for the third sensor

        # Initialize sensor objects with respective data
        sensor1 = Sensor(sensor_type=SensorType(name="Air Quality", units="ppm"), location="Indoor", data=data_sensor1)
        sensor2 = Sensor(sensor_type=SensorType(name="Temperature", units="Celsius"), location="Living Room", data=data_sensor2)
        sensor3 = Sensor(sensor_type=SensorType(name="Rainfall", units="mm"), location="Backyard", data=data_sensor3)

        # Add sensors to the list of IoT device sensors
        self.sensors.extend([sensor1, sensor2, sensor3])

    def collect_data(self):
        for sensor in self.sensors:
            data_point = sensor.get_data()  # Get data from the sensor
            sensor.add_data(data_point)  # Add data to the sensor
            self.data_collector.add_sensor_data(sensor, data_point)  # Add data to the data collector

    def transmit_data(self, central_system):
        central_system.receive_data(self.data_collector)


def main(max_iterations, filename):
    device1 = IoTDevice(device_id=1)
    data_collector = device1.data_collector
    central_system = CentralSystem(data_collector)

    for _ in range(max_iterations):
        try:
            device1.collect_data()
            device1.transmit_data(central_system)
        except Exception as e:
            print("An error occurred:", e)
            continue

    central_system.save_report_to_file(filename)


if __name__ == "__main__":
    max_iterations = 10
    filename = "results.txt"
    main(max_iterations, filename)
