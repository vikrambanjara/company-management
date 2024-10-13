from django.db import models

# Create your models here.

#creating company model...
class company(models.Model):
  company_id  = models.AutoField(primary_key=True)
  name        = models.CharField(max_length=50)
  location    = models.CharField(max_length=40)
  about       = models.CharField(max_length=100)
  type        = models.CharField(max_length=50, choices=
                                 (("IT","IT"),
                                 ("Non IT","Non IT"),
                                 ("Auto mobile","auto mobile")
                                  ))
  added_date  = models.DateTimeField(auto_now=True)
  active      = models.BooleanField(default=True)
  def __str__(self):
    return self.name+'__'+self.location
  

#employe's model...
class Employe(models.Model):
  name         = models.CharField(max_length=50)
  email        = models.CharField(max_length=50)
  address      = models.CharField(max_length=200)
  phone        = models.CharField(max_length=15)
  about        = models.TextField(max_length=100)
  About_company= models.ForeignKey(company,on_delete=models.CASCADE)
  position     = models.CharField(max_length=50, choices=
                                 (('manager','manager'),
                                 ('softwere developer','softwere developer'),
                                 ('HR','HR'),
                                 ('beldar','beldar')))
  def __str__(self):
    return self.name
  