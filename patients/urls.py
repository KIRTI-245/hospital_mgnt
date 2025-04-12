from django.urls import path
from .views import PatientCreate, PatientList, PatientDetail, PatientUpdate, PatientDelete

urlpatterns = [
    path('lists/', PatientList.as_view(), name='patient_list'),
    path('create/', PatientCreate.as_view(), name='patient_create'),
    path('detail/<int:pk>/', PatientDetail.as_view(), name='patient_detail'),
    path('update/<int:pk>/', PatientUpdate.as_view(), name='patient_update'),
    path('delete/<int:pk>/', PatientDelete.as_view(), name='patient_delete'),    
]
