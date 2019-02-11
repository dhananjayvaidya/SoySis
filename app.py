from flask import Flask
import logging as logger

logger.basicConfig(level="DEBUG")

flaskAppInstance = Flask(__name__)

if __name__ == '__main__':
    logger.debug("Starting the Application")
    from api import *
    from frontend import *
    flaskAppInstance.run(host="0.0.0.0", port=6000,debug=True,use_reloader=True)