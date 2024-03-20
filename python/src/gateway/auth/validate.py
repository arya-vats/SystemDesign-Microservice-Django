import os, requests

def token(requests):
	if not "Authorization" in request.headers:
		return "misisng credentials", 401
	token = request.headers["Authorization"]