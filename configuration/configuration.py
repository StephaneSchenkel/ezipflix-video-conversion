import yaml
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)


class Configuration(object):
    def __init__(self):
        self.configuration_file = "C:\\Users\\SStephane\\Documents\\Archi\\video-conversion\\application.yml" # Euuuuuurk !
        self.configuration_data = None

        f = open(self.configuration_file, 'r')
        self.configuration_data = yaml.load(f.read())
        f.close()

    def get_database_host(self):
        return self.configuration_data['spring']['data']['mongodb']['host']

    def get_database_port(self):
        return self.configuration_data['spring']['data']['mongodb']['port']

    def get_database_name(self):
        return self.configuration_data['spring']['data']['mongodb']['database']

    def get_subscription_id(self):
        return self.configuration_data['conversion']['messaging']['googlepubsub']['subscription-id']

    def get_project_id(self):
        return self.configuration_data['conversion']['messaging']['googlepubsub']['project-id']

    def get_video_conversion_collection(self):
        return self.configuration_data['spring']['data']['mongodb']['collections']['video-conversions']

    def get_video_status_callback_url(self):
        return self.configuration_data['conversion']['messaging']['video-status']['url']
