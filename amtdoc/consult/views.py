from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from consult.models import Consultation
from agency.models import Agent, Patient, Doctor
from consult.serializers import ConsultationSerializer

@csrf_exempt
def consultation_list(request, status=None):
	"""
	List all consultations of certain status
	or create a new request
	"""
	if request.method == 'GET':
		if status is None:
			consultations = Consultation.objects.all()
		else:
			consultations = Consultation.objects.filter(status=status)
		serializer = ConsultationSerializer(consultations, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ConsultationSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def consultation_detail(request, pk):
	"""
	Retrieve, update or delete a consultation
	"""
	try:
		consultation = Consultation.objects.get(pk=pk)
	except Consultation.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ConsultationSerializer(consultation)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ConsultationSerializer(consultation, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		consultation.delete()
		return HttpResponse(status=204)

@csrf_exempt
def update_consultation_status(request, pk, status=None):
	"""
	Accepts a consultation
	"""
	try:
		consultation = Consultation.objects.get(pk=pk)
	except Consultation.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'PUT':
		if status is None:
			consultation.status += 1
		else:
			consultation.status = status
		consultation.save()
		serializer = ConsultationSerializer(consultation)
		return JsonResponse(serializer.data)

def doctors_view(request):
	"""
	For demonstration purposes. Loads doctor's page
	"""
	template = loader.get_template("doctor/doctor.html")
	consultations = Consultation.objects.filter(status=0)
	context = {
		"base_url": request.build_absolute_uri('/'),
		"consultations": consultations
	}
	return HttpResponse(template.render(context, request))

def doctors_call(request, meetingId):
	# meetingId = request.get()
	template = loader.get_template("doctor/call.html")
	context = {
		"meetingId": meetingId
	}
	return HttpResponse(template.render(context, request))