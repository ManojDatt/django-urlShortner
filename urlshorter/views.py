from django.shortcuts import render
from .base_converter import *
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.views import View
from urlparse import urlparse
from urlshorter.models import *
import base64
# from mongoengine.django.shortcuts import get_document_or_404
class IndexView(View):
	template_name = 'index.html'
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name)
	def post(self, request, *args, **kwargs):
		host = 'http://localhost:8000/'
		original_url = request.POST['url']
		bases = urlparse(original_url)
		if bases.scheme == '':
			url = 'http://'+original_url
			res=ShortenedUrls.objects.create(web_url=base64.urlsafe_b64encode(url))
			print("======================",res.id)
			# encoded_string = base62(res.id)
			# print(encoded_string)
			short_url=host+str(res.id)
			return render(request, self.template_name, {'short_url': short_url})
		elif bases.scheme=='http' or bases.scheme=='https':
			url=original_url
			res=ShortenedUrls.objects.create(web_url=base64.urlsafe_b64encode(url))
			print("======================",res.id)
			# encoded_string = base62(res.id)
			short_url=host+str(res.id)
			return render(request, self.template_name, {'short_url': short_url})
		else:
			return render(request, self.template_name)
		
		

class ShortView(View):
	def get(self,request,short_url):
		# decoded_id = base10(short_url)
		url = 'http://localhost:8000'
		res = ShortenedUrls.objects.get(id=short_url)
		uenc = unicode(res.web_url)
		url = base64.urlsafe_b64decode(uenc.encode("ascii"))
		return redirect(url)