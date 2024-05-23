from django.urls import path
from consult import views

urlpatterns = [
	path('api/consult/', views.consultation_list),
	path('api/consult/status/<int:status>/', views.consultation_list),
	path('api/consult/<int:pk>', views.consultation_detail),
	path('api/consult/status/<int:pk>/<int:status>', views.update_consultation_status),
	path('consult/doctor/', views.doctors_view),
	path('consult/doctor/call/<meetingId>', views.doctors_call),
]
