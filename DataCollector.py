class DataCollector:
    def __init__(self):
        self.collected_data = {}

    def add_sensor_data(self, sensor, data):
        """
        Add sensor data to the collected data dictionary.
        """
        self.collected_data[sensor] = data

    def get_collected_data(self):
        """
        Get the collected data dictionary.
        """
        return self.collected_data
