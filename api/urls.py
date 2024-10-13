from django.contrib import admin
from django.urls import path,include
from api.views import companyViewset,employeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', companyViewset)
router.register(r'employees', employeViewset)

urlpatterns = [
    path('', include(router.urls)),
]