from django.db import models
from agency.models import User, Patient, Doctor


# class Doctor(models.Model):
# 	user = models.OneToOne(User, on_delete=models.CASCADE)
# 	name = models.CharField(max_length=255)

class Consultation(models.Model):

	CONSULTATION_STATUS_CHOICES = (
		(0, 'requested'),
		(1, 'accepted'),
		(2, 'ongoing'),
		(3, 'ended'),
	)

	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True)
	starttime = models.DateTimeField(auto_now_add=True)
	endtime = models.DateTimeField(blank=True, null=True)
	notes = models.TextField()
	status = models.IntegerField(choices=CONSULTATION_STATUS_CHOICES, default=0)

	class Meta:
		ordering = ['starttime']

	@property
	def meeting_id(self):
		return "meeting_" + self.pk

