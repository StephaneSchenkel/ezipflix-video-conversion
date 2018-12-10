from google.cloud import datastore
import logging
import time

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)

class VideoConversionDatabase(object):

    def __init__(self, _config_):
        self.entity_name = _config_.get_entity_name()
        self.client = datastore.Client(_config_.get_project_id())

    def update(self, id, targetFilename, bucket):
        key = self.client.key(self.entity_name, int(id))
        video_conversion = self.client.get(key)

        if not video_conversion:
            logging.error('video_conversion {} does not exist in datastore.'.format(id))

        video_conversion.update({
            'tstamp': time.time(),
            'targetFilename': targetFilename,
            'bucket': bucket
        })

        self.client.put(video_conversion)
