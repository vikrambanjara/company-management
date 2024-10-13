from rest_framework import serializers
from api.models import company,Employe
class companySerializer(serializers.ModelSerializer):
  class Meta:
    model  = company
    fields = "__all__"

class employeSerializer(serializers.ModelSerializer):
  class Meta:
    model  = Employe
    fields  ="__all__"