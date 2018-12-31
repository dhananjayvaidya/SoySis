#!/usr/bin/python3
from flask_restful import Resource
from flask import Flask, request, jsonify
from json import dumps
from .service import AppConfigService

class TwitterConfiguration(Resource):
    def post(self):
        Con = AppConfigService.AppConfigService()

        #fetch data from request
        consumer_key        = request.json['consumer_key']
        consumer_secret     = request.json['consumer_secret']
        access_token        = request.json['access_token']
        access_token_secret = request.json['access_token_secret']

        if Con.setTwitterDetails(consumer_key,consumer_secret,access_token,access_token_secret) == True :
            return {"message":"Successfully Saved"},200
        else:
            return {"message":"problem occur"},500
    def get(self):
        Con = AppConfigService.AppConfigService()

        t = Con.getTwitterDetails()
        return t