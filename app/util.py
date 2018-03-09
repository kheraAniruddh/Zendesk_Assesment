__author__ = "Aniruddh Khera"

""" This modules handles requests to the Zendesk APIs """
""" Basic authentication is used to make successful request to the zendesk APIs """
from flask import abort
import requests
import json
from . import config
Conf = config.Config()


def makeRequest(URL):
	""" Util function validating the request """
	try:
		response = requests.get(URL, auth=(Conf.AGENT_EMAIL, Conf.AGENT_PASSWORD))
	except requests.exceptions.RequestException as e:
		print(e)
		abort(500)

	result = json.loads(response.content.decode('utf-8'))
	if response.status_code == 401:
		return  abort(401)
	if response.status_code == 400:
		return result.get('error')
	return result


 	