from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ShortAPIView,IndexAPIView,ListObjectAPIView
urlpatterns = [
    url(r'^generator/$', IndexAPIView.as_view()),
    url(r'^generator/(?P<short_url>.*)/$', ShortAPIView.as_view()),
    url(r'^lists/$',ListObjectAPIView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)