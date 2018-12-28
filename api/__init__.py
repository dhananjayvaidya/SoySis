from flask_restful import Api

from app import flaskAppInstance
from .Task import Task
from .Sentiment import Sentiment
restServer = Api(flaskAppInstance)
restServer.add_resource(Sentiment,"/api/sentiment")
restServer.add_resource(Task,"/api/v1.0/task")