from django.db import models

class ShortenedUrls(models.Model):
	web_url = models.CharField(('Original Url'),max_length=200,blank=False)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)
