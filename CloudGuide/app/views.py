from django.shortcuts import render
from CloudGuide.app.models import Topics,SubTopic
from rest_framework import viewsets
from CloudGuide.app.serializers import TopicsSerializer,SubTopicsSerializer


class TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Topics.objects.all()
    serializer_class = TopicsSerializer
    

class subViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SubTopic.objects.all()
    serializer_class = SubTopicsSerializer