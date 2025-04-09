
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

urlpatterns = [
     path('', lambda request: HttpResponse("welcome to doctor")),
    path("admin/", admin.site.urls),
    path("api/doctor/", include("doctor.urls")),

]
