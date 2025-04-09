from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.response import Response

class DoctorCreate(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorLists(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = [{"id": dt["id"], "doctorName": dt["doctorName"], "speciality": dt["speciality"], "education": dt["education"], "experience": dt["experience"], "contact": dt["contact"]} for dt in serializer.data]
        return Response(data)

class DoctorDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class DoctorUpdate(generics.UpdateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        response = super().update(request, *args, **kwargs)
        response.data['message'] = "Doctor details updated successfully"
        response.data['status'] = 200
        return response

class DoctorDelete(generics.DestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def delete(self, request, *args, **kwargs):
        return Response({"message": "Doctor deleted successfully", "status": 200})