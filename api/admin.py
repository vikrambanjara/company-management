from django.contrib import admin
from api.models import company,Employe

# Register your models here.

class companyAdmin(admin.ModelAdmin):
  list_display=('name','location','type')
  search_fields=('name',)
  

class employeAdmin(admin.ModelAdmin):
  list_display=('name','email','About_company')


admin.site.register(company,companyAdmin)
admin.site.register(Employe,employeAdmin)