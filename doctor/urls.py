from django.urls import path
from .views import DoctorCreate, DoctorLists, DoctorDetails, DoctorUpdate, DoctorDelete
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("welcome to doctor")),
    path('create/', DoctorCreate.as_view(), name='doctor_create'),
    path('lists/', DoctorLists.as_view(), name='doctor_lists'),
    path('details/<int:pk>/', DoctorDetails.as_view(), name='doctor_details'),
    path('update/<int:pk>/', DoctorUpdate.as_view(), name='doctor_update'),
    path('delete/<int:pk>/', DoctorDelete.as_view(), name='doctor_delete'),
]

