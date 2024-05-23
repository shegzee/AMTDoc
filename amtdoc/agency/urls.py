from django.urls import path
from .views import (
    AgentSignUpView,
    AgentLoginView,
    AddPatientView,
    AgentPatientListView,
    PatientDetailView,
)

urlpatterns = [
    path('agent-signup/', AgentSignUpView.as_view(), name='agent-signup'),
    path('agent-login/', AgentLoginView.as_view(), name='agent-login_token_obtain_pair'),
    path('agent-patients/add/', AddPatientView.as_view(), name='add-patient'),
    path('agent-patients/list/', AgentPatientListView.as_view(), name='agent-patient-list'),
    path('agent-patient/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
]