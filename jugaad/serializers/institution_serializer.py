from jugaad.models import Institution
from rest_framework import serializers

class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Institution
        fields = ['name']