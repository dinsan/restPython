from rest_framework import serializers
from CloudGuide.app.models import Topics,SubTopic

class SubTopicsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubTopic
        fields = ('__all__')


class TopicsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topics
        fields = ('__all__')