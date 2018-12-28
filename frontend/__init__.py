from flask_restful import Api

from app import flaskAppInstance

restServer = Api(flaskAppInstance)
