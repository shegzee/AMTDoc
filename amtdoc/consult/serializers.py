from .models import Doctor, Consultation
from rest_framework import serializers

class ConsultationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Consultation
		fields = '__all__'

