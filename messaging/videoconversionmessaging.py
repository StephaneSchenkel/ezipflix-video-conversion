import time
from threading import Thread
import logging
import json
from google.cloud import pubsub_v1

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)

class VideoConversionMessaging(Thread):
    def __init__(self, _config_, converting_service):
        Thread.__init__(self)

        self.subscriber = pubsub_v1.SubscriberClient()
        self.subscription_path = self.subscriber.subscription_path(_config_.get_project_id(), _config_.get_subscription_id())

        self.converting_service = converting_service
        self.consuming = "_CONSUMING_"
        self.start()

    def run(self):
        if "_CONSUMING_" == self.consuming :
            self.subscriber.subscribe(self.subscription_path, callback=self.on_message)
            while True:
                time.sleep(60)

    def on_message(self,  message):
        message.ack()
        logging.info(message)
        logging.info('URI = %s', message.data)
        convert_request = json.loads(message.data)
        logging.info(convert_request)
        self.converting_service.convert(convert_request["id"], convert_request['originFilename'], convert_request['bucket'])

    def stop_consuming(self):
        logging.info("Stops consuming on message bus")
        self.consuming = "_IDLE_"

    def start_consuming(self):
        logging.info("Starts consuming on message bus")
        self.consuming = "_CONSUMING_"

    def is_consuming(self):
        return self.consuming
