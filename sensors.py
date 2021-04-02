class Sensors:
    def __init__(self, **kwargs):
        self.sensor_data_dictionary = kwargs

    def update(self, **kwargs):
        self.sensor_data_dictionary = kwargs

    def get_value(self, key):
        return (self.sensor_data_dictionary.get(key))
