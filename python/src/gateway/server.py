import os, gridfs, pika, json
from flask import Flask, request
from flask_pymongo import Pymongo
from auth import validate
from auth_svc import access
from storage import util


server = Flask(__name__)
server.config["MONGO_URI"] = "mongodb://host.minikube.internal:27017/videos"

mongo = Pymongo(server)

fs = gridfs.GridFS(mongo.db)

connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
channel = connection.channel()

@server.route("/login", methods=["POST"])
def login():
	token, err = access.login(request)

	if not err:
		return token
	else:
		return err


@server.route("u/pload", methods=["POST"])
def upload():
	access, err = validate.token(request)







