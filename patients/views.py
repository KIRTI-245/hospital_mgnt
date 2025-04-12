from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer

class PatientCreate(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientList(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDetail(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientUpdate(generics.UpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientDelete(generics.DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer