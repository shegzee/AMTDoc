from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Agent, Patient, Doctor, Lga

admin.site.register(User, UserAdmin)
admin.site.register(Agent)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Lga)
