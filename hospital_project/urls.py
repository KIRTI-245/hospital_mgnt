
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
     path('', lambda request: HttpResponse("welcome to doctor")),
    path("admin/", admin.site.urls),
    path("doctor/", include("doctor.urls")),
    path("patient/", include("patients.urls")),

]
