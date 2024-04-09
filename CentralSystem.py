class CentralSystem:
    def __init__(self, data_collector):
        self.data_collector = data_collector
        self.reports = []

    def receive_data(self, data_collector):
        """
        Receive data from a data collector.
        """
        self.data_collector = data_collector

    def generate_report(self):
        """
        Generate a report based on the collected data.
        """
        collected_data = self.data_collector.get_collected_data()
        report = ""
        for sensor, data in collected_data.items():
            report += f"Sensor: {sensor}, Data: {data}\n"
        return report

    def save_report_to_file(self, filename):
        """
        Save the generated report to a file.
        """
        report = self.generate_report()
        with open(filename, 'w') as f:
            f.write(report)
