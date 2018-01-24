

import logging

from autobahn.asyncio.websocket import WebSocketClientProtocol, \
    WebSocketClientFactory

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', level=logging.DEBUG)
logging.getLogger("pika").setLevel(logging.INFO)

class VideoStatusWebsocket(WebSocketClientProtocol):

    def send(self, jsonpayload):
        self.sendMessage(jsonpayload.encode('utf8'))

    def onOpen(self):
        #self.sendHello()
        logging.info("Websocket session is opened.")


    def onMessage(self, payload, isBinary):
        if not isBinary:
            print("Text message received: {}".format(payload.decode('utf8')))


