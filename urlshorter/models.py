from django.db import models
from mongoengine import *
class ShortenedUrls(Document):
	web_url = StringField(required=True)
	created_at = DateTimeField(auto_now=True)
	updated_at = DateTimeField(auto_now=True)
