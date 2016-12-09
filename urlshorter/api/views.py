from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from urlshorter.base_converter import *
from urlparse import urlparse
from urlshorter.models import *
import base64

class IndexAPIView(APIView):
	def post(self, request, format=None):
		params = request.data  
		host = 'http://localhost:8000/'
		original_url = params['url']
		bases = urlparse(original_url)
		if bases.scheme == '':
			url = 'http://'+original_url
			res=ShortenedUrls.objects.create(web_url=base64.urlsafe_b64encode(url))
			encoded_string = base62(res.id)
			short_url=host+encoded_string
			return Response({"message":"Your shor url generated.","short_url": short_url,"code":200})
		elif bases.scheme=='http' or bases.scheme=='https':
			url=original_url
			res=ShortenedUrls.objects.create(web_url=base64.urlsafe_b64encode(url))
			encoded_string = base62(res.id)
			short_url=host+encoded_string
			return Response({"message":"Your shor url generated.","short_url": short_url,"code":200})
		else:
			return Response({"message":"Either invalid Url Or Invalid character entered.","code":401})
		
		

class ShortAPIView(APIView):
	def get(self,request,short_url,format=None):
		decoded_id = base10(short_url)
		url = 'http://localhost:8000'
		res = get_object_or_404(ShortenedUrls,id=decoded_id)
		uenc = unicode(res.web_url)
		url = base64.urlsafe_b64decode(uenc.encode("ascii"))
		return Response({"message":"Your redirecting Original Url","url": url,"code":200})