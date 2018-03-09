__author__ = "Aniruddh Khera"
""" This modules contains the happy path test cases """

import app
import unittest
import json

class AppTestCase(unittest.TestCase):
	
	def setUp(self):
		app.app.testing = True
		self.app = app.app.test_client()
		self.viewTicket = "{'url': 'https://ak5146.zendesk.com/api/v2/tickets/1.json', 'id': 1, 'external_id': None, 'via': {'channel': 'sample_ticket', 'source': {'from': {}, 'to': {}, 'rel': None}}, 'created_at': '2018-03-04T01:45:54Z', 'updated_at': '2018-03-04T01:45:54Z', 'type': 'incident', 'subject': 'Sample ticket: Meet the ticket', 'raw_subject': 'Sample ticket: Meet the ticket', 'description': 'Hi Anirudh,\n\nEmails, chats, voicemails, and tweets are captured in Zendesk Support as tickets. Start typing above to respond and click Submit to send. To test how an email becomes a ticket, send a message to support@ak5146.zendesk.com.\n\nCurious about what your customers will see when you reply? Check out this video:\nhttps://demos.zendesk.com/hc/en-us/articles/202341799\n', 'priority': 'normal', 'status': 'open', 'recipient': None, 'requester_id': 361436053951, 'submitter_id': 361423841471, 'assignee_id': 361423841471, 'organization_id': None, 'group_id': 360000414111, 'collaborator_ids': [], 'follower_ids': [], 'forum_topic_id': None, 'problem_id': None, 'has_incidents': False, 'is_public': True, 'due_at': None, 'tags': ['sample', 'support', 'zendesk'], 'custom_fields': [], 'satisfaction_rating': None, 'sharing_agreement_ids': [], 'fields': [], 'followup_ids': [], 'brand_id': 360000253811, 'allow_channelback': False}"


	def test_index(self):
		response  = self.app.get('/')
		assert '200 OK' in response.status


	def test_viewTicket(self):
		response = self.app.get('/viewticket?ticketId=1')
		assert '200 OK' in response.status
		

	def test_viewAllTickets(self):
		response = self.app.get('/viewtallickets?page=1')
		assert '200 OK' in response.status

		
