#!/usr/bin/python3.5

import logging

from configuration.configuration import Configuration
from messaging.videoconversionmessaging import VideoConversionMessaging
from engine.videoconversion import VideoConversion
from videoconvunixsocket.videoconversionunixsocket import VideoConversionUnixSocket
from filesystem.videoconversionfilesystem import VideoConversionFilesystem
from database.videoconversiondatabase import VideoConversionDatabase


if __name__ == '__main__':

    logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)
    configuration = Configuration()

    logging.info(configuration.get_project_id())
    logging.info(configuration.get_subscription_id())
    logging.info(configuration.get_entity_name())

    video_unix_socket = VideoConversionUnixSocket()
    video_conversion_fs = VideoConversionFilesystem()
    video_conversion_database = VideoConversionDatabase(configuration)
    video_unix_socket.start()
    video_conversion_service = VideoConversion(configuration, video_conversion_fs, video_conversion_database)
    video_messaging = VideoConversionMessaging(configuration, video_conversion_service)
    video_unix_socket.setVideoConversionMessaging(video_messaging)

