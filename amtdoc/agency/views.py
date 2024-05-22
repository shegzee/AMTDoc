from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer, AgentSerializer, PatientSerializer, DoctorSerializer, LgaSerializer 
from .models import User, Agent, Patient, Doctor
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated

class AgentSignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            lga_data = request.data.get('lga', None)
            if lga_data:
                lga_serializer = LgaSerializer(data={'name': lga_data})
                if lga_serializer.is_valid():
                    lga = lga_serializer.save()
                else:
                    return Response(lga_serializer.errors, status=400)
            else:
                lga = None

            agent_data = request.data.copy()
            agent_data.pop('username', None)
            agent_data.pop('email', None)
            agent_data.pop('password', None)
            agent_data.pop('lga', None)
            Agent.objects.create(user=user, lga=lga, **agent_data)
            return Response({'message': 'Agent registered successfully.'})
        else:
            return Response(serializer.errors, status=400)


class AgentLoginView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response(serializer.errors, status=400)


class AddPatientView(generics.CreateAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()



class AgentPatientListView(generics.ListAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        agent = Agent.objects.get(user=self.request.user)
        return Patient.objects.filter(agent=agent)


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()    
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        agent = Agent.objects.get(user=self.request.user)
        return Patient.objects.filter(agent=agent)