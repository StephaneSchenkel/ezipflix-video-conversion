import yaml
import logging
import os

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)


class Configuration(object):
    def __init__(self):
        self.configuration_file = os.getcwd() + "/application.yml"
        logging.info(self.configuration_file)
        self.configuration_data = None

        f = open(self.configuration_file, 'r')
        self.configuration_data = yaml.load(f.read())
        f.close()

    def get_subscription_id(self):
        return self.configuration_data['conversion']['messaging']['google']['subscription-id']

    def get_project_id(self):
        return self.configuration_data['conversion']['messaging']['google']['project-id']

    def get_video_status_callback_url(self):
        return self.configuration_data['conversion']['messaging']['video-status']['url']

    def get_entity_name(self):
        return self.configuration_data['conversion']['data']['google']['entity-name']
