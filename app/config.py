import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

class Config:
	AGENT_EMAIL= os.environ.get("AGENT_EMAIL")
	AGENT_PASSWORD = os.environ.get("AGENT_PASSWORD")
	ZENDESK_BASE_URL = os.environ.get("ZENDESK_BASE_URL")