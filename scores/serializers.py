from rest_framework import serializers

from .models import Situation

class SituationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Situation
        fields = ('target','runs','wickets','avg_socre','created_at'
)
