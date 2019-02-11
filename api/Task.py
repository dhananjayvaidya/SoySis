from flask_restful import Resource
import logging as logger
class Task(Resource):
    
    def get(self):
        logger.debug("Inside get method")
        return {"message" : "Inside Get Method"},200

    def post(self):
        logger.debug("Inside post method")
        return {"message" : "Inside Post Method"},200
    
    def put(self):
        logger.debug("Inside Put method")
        return {"message" : "Inside Put Method"},200
    
    def delete(self):
        logger.debug("Inside Delete method")
        return {"message" : "Inside Delete Method"},200

    