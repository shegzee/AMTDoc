from django.urls import path
from consult import views

urlpatterns = [
	path('consult/', views.consultation_list),
	path('consult/<int:pk>/', views.consultation_detail),
]