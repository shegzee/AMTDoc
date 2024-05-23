from .models import Consultation
from agency.models import Patient
from rest_framework import serializers
from agency.serializers import PatientSerializer


class ConsultationSerializer(serializers.ModelSerializer):
	#patient = PatientField(many=False, queryset=Patient.objects.all())
	class Meta:
		model = Consultation
		#fields = ('patient', 'notes', 'status')
		fields = '__all__'

