import logging
import ffmpy
import websocket
import json

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)
#  ffmpeg -i Game.of.Thrones.S07E07.1080p.mkv -vcodec mpeg4 -b 4000k -acodec mp2 -ab 320k converted.avi


class VideoConversion(object):
    def __init__(self, _config_, _fs_service_, _db_service_):
        self.url = _config_.get_video_status_callback_url()
        self.fs_service = _fs_service_
        self.db_service = _db_service_

    def convert(self, _id_, _filename_, _bucket_):
        self.fs_service.downloadfile(_filename_, _bucket_)

        converted = _filename_.replace(".mkv", "-converted.avi")
        logging.info('ID = %s, URI = %s —› %s',  _id_, _filename_ , converted )
        ff = ffmpy.FFmpeg(
                inputs={_filename_: None},
                outputs={converted : '-y -vcodec mpeg4 -b 4000k -acodec mp2 -ab 320k' }
            )
        logging.info("FFMPEG = %s", ff.cmd)
        ff.run()

        self.fs_service.uploadfile(converted, _bucket_)

        self.db_service.update(_id_, converted, _bucket_)

        payload = dict()
        payload["id"] = _id_;
        payload["status"] = 0;

        json_payload = json.dumps(payload)
        logging.info("payload = %s", json_payload)

        ws = websocket.create_connection(self.url)
        ws.send(json_payload);
        ws.close()
