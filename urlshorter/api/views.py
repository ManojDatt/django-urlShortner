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
		print(bases)
		if bases.scheme == '':
			url = 'http://'+original_url
			res=ShortenedUrls.objects.create(web_url=base64.urlsafe_b64encode(url))
			
			short_url=host+str(res.id)
			return Response({"message":"Your shor url generated.","short_url": short_url,"code":200})
		elif bases.scheme=='http' or bases.scheme=='https':
			url=original_url
			res=ShortenedUrls.objects.create(web_url=base64.urlsafe_b64encode(url))
			encoded_string = str(res.id)
			short_url=host+encoded_string
			return Response({"message":"Your shor url generated.","short_url": short_url,"code":200})
		else:
			return Response({"message":"Either invalid Url Or Invalid character entered.","code":401})
		
		

class ShortAPIView(APIView):
	def get(self,request,short_url,format=None):
		
		url = 'http://localhost:8000'
		res = ShortenedUrls.objects.get(id=short_url)
		uenc = unicode(res.web_url)
		url = base64.urlsafe_b64decode(uenc.encode("ascii"))
		return Response({"message":"Your redirecting Original Url","url": url,"code":200})

from .serializers import *
from rest_framework_mongoengine import generics as drfme_generics
from rest_framework import generics
class ListObjectAPIView(generics.ListAPIView):
	queryset = ShortenedUrls.objects
	serializer_class = ShortenedUrlsSerializer
       