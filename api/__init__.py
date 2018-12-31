from flask_restful import Api

from app import flaskAppInstance

from .Sentiment import Sentiment
from .Configuration import TwitterConfiguration

restServer = Api(flaskAppInstance)
restServer.add_resource(TwitterConfiguration,"/api/twiiter/config")
restServer.add_resource(Sentiment,"/api/sentiment")
