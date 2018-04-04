__author__ = "Aniruddh Khera"

""" This modules handles APIs for listing all the tickets and viewing a single ticket details """

from flask import Flask, request, render_template, abort
import json
from . import config
from . import util

Conf = config.Config()

app = Flask(__name__, static_folder = "../static", template_folder = "../templates")

@app.route('/')
def index():
	""" Simple landing page route, displays USERNAME """
	print('in here')
	name = None
	return render_template("index.html", name = Conf.AGENT_EMAIL)


@app.route('/viewalltickets')
def viewAllTickets():
	""" View handler for listing all the tickets"""
	""" @queryParam = page """

	result = None
	if 'page' in request.args:
		pageNo = request.args.get('page')
	else:
		return abort(404)	
	result = util.makeRequest(Conf.ZENDESK_BASE_URL + 'tickets.json?page='+pageNo)	
	return render_template("viewalltickets.html",  result = result)
	


@app.route('/viewticket')
def viewTicketDetails():
	""" View handler for viewing a single ticket"""
	""" @queryParam = ticketId """

	result = None
	if 'ticketId' in request.args:
		ticketId = request.args.get('ticketId')
	else:
		return abort(404)
	result = util.makeRequest(Conf.ZENDESK_BASE_URL + 'tickets/'+ ticketId+'.json')
	if(result.get('ticket') != None):
		return  render_template("viewticket.html",  result = result.get('ticket'))
	else:	
		return  render_template("viewticket.html",  result = result)


@app.errorhandler(401)
def pageNotFound(error):
	""" Handles unauthorized access """
	return render_template('error.html', result = error)


@app.errorhandler(404)
def pageNotFound(error):
	""" Handles could not find requests """ 
	return render_template('error.html', result = error)


@app.errorhandler(500)
def pageNotFound(error):
	""" Handles unexpected server errors """
	return render_template('error.html', result = error)		
