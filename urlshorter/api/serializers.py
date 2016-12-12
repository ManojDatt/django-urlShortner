from rest_framework_mongoengine.serializers import DocumentSerializer
from urlshorter.models import *
class ShortenedUrlsSerializer(DocumentSerializer):
    class Meta:
        model = ShortenedUrls
        fields = '__all__' 
        depth = 2